from django.shortcuts import render
import pickle
from django.http import JsonResponse
from .models import LLDP
import networkx as nx
import re
#init
with open("graph.pkl", 'rb') as file:
    graph = pickle.load(file)

unique_nodes = list(graph.nodes)
unique_nodes.remove('root_cor')

def get_isolated_nodes():
    root_cor = 'root_cor'
    visited_nodes = set()
    def dfs(node):
        visited_nodes.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited_nodes:
                dfs(neighbor)

    dfs(root_cor)
    nodes_without_path = [node for node in graph.nodes if node != root_cor and node not in visited_nodes]
    return nodes_without_path

isolated_nodes = get_isolated_nodes() 

#views
def home(request):
    return render(request, 'topology/home.html', {"unique_nodes":unique_nodes, 'isolated_nodes':isolated_nodes})

def get_devices(request):
    all_nodes = LLDP.objects.all()
    devices = []
    seen_nodes = set()  

    for node in all_nodes:
        if node.device_a_name != "":
            device = {'node': node.device_a_name, 'ip': node.device_a_ip}
        else:
            device = {'node': node.device_b_name, 'ip': node.device_b_ip}
        
        if device['node'] not in seen_nodes:
            devices.append(device)
            seen_nodes.add(device['node'])

    return JsonResponse(devices, safe=False)

def get_graph(request):
    get_node = request.GET.get('node')

    context = {
            'nodes': [],
            'edgesData': [],
            'shortestPath': [],
            'secondShortestPath': []
        }
    try:
        first_shortest = nx.shortest_path(graph, get_node, 'root_cor')
        shortest = second_shortest_path(graph, get_node, first_shortest[-2])        # for alternative path to same ICOR
        # shortest = second_shortest_path(graph, get_node, 'root_cor')                 # for second shortest path
        neighbours = [i for i in graph.neighbors(get_node)]
        print("First Shortest Path:", shortest[0])
        if shortest[0] != shortest[1] and len(shortest[0]) != len(shortest[1]):
            print("Second Shortest Path:", shortest[1])
            second_shortest = shortest[1]
        else:
            print('No Alternative Path')
            second_shortest = []
        nodes, edgesData, shortestPath, secondShortestPath = convert_data(neighbours, shortest[0], second_shortest, get_node)

        context = {
            'nodes': nodes,
            'edgesData': edgesData,
            'shortestPath': shortestPath,
            'secondShortestPath': secondShortestPath,
            'node_name': get_node
        }
        return JsonResponse(context)
    except nx.NetworkXNoPath:
        print('No Path to ICOR')
        neighbours = [i for i in graph.neighbors(get_node)]
        nodes, edgesData, shortestPath, secondShortestPath = convert_data(neighbours, [], [], get_node)

        context = {
            'nodes': nodes,
            'edgesData': edgesData,
            'shortestPath': shortestPath,
            'secondShortestPath': secondShortestPath,
            'node_name': get_node
        }
        return JsonResponse(context)

#function
def second_shortest_path(graph, source, target):
    shortest_path = nx.shortest_path(graph, source=source, target=target , weight='weight')
    for u, v in zip(shortest_path[:-1], shortest_path[1:]):
        graph[u][v]['weight'] = float('inf')
    second_shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    for u, v in zip(shortest_path[:-1], shortest_path[1:]):
        graph[u][v]['weight'] = 1
    

    if 'root_cor' in second_shortest_path:
         second_shortest_path = []

    return shortest_path, second_shortest_path

def convert_data(neighbours, first_shortest_path, second_shortest_path, get_node):
    unique_nodes = list(set(neighbours + first_shortest_path + second_shortest_path + [get_node]))
    
    nodes = [
        {"id": node, "label": node, "color": {"background": 'red', "border": 'black'}} if "ICOR" in node else 
        {"id": node, "label": node, "font": {"color": 'red'}, "color": {"background": 'green', "border": 'black'}} if node == get_node else 
        {"id": node, "label": node}
        for node in unique_nodes
    ]
    def create_edges(path, neighbour=False):
        if neighbour:
            return [{"from": path[-1], "to": path[i], "arrows": "to, from"} for i in range(len(path)-1)]
        else:
            return [{"from": path[i], "to": path[i+1], "arrows": "to, from"} for i in range(len(path)-1)]

    neighbours.append(get_node)
    edges_list = []

    edges_list += create_edges(first_shortest_path)
    edges_list += create_edges(second_shortest_path)

    edges_list += create_edges(neighbours, True)

    unique_edges = []
    for edge in edges_list:
        if edge not in unique_edges:
            unique_edges.append(edge)

    shortestPath = first_shortest_path
    secondShortestPath = second_shortest_path
    return nodes, unique_edges, shortestPath, secondShortestPath
