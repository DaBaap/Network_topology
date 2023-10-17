import networkx as nx
from topology.models import LLDP
import pickle
def build_graph():
    kingdom_graph = nx.Graph()

    kingdom_graph.add_node('root_cor')
    cor_root = []
    connections = LLDP.objects.values('device_a_name', 'device_b_name')

    for i in connections:
        kingdom_graph.add_edge(i["device_a_name"], i["device_b_name"])

        
        if "ICOR" in i["device_a_name"] and i["device_a_name"] not in cor_root:
            kingdom_graph.add_edge(i["device_a_name"], 'root_cor')
            cor_root.append(i["device_a_name"])

        elif "ICOR" in i["device_b_name"] and i["device_b_name"] not in cor_root:
            kingdom_graph.add_edge(i["device_b_name"], 'root_cor')
            cor_root.append(i["device_b_name"])

    with open('graph.pkl', 'wb') as file:
        pickle.dump(kingdom_graph, file)