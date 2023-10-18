# Network_topology
Task 1

## Introduction
The Web Application is created in Django Framework. The Application is to visualize the network topology of Nodes and help find the shortest path to ICOR. Additionally, the application of alternative path to same ICOR can also be visualized. Moreover, isoloted nodes can also be seen in the table.

## Methodology
The Web Application uses networkx for network graph creation and visjs for visualization. The whole app contains one page for user friendly behaviour. The approach taken was slightly different from the requirements however all the functionality can be seen in the application.

## Usage
Install the python packages from req.txt file. 

If there is a csv file to be loaded in database then run (the project already contains the sqlite database that was provided):
    ```python manage.py import_csv <filename.csv>```

Run the server:
    ```python manage.py runserver```

### Path through table
In the web page you can see list of nodes/isolated nodes, search bar and a section for network graph. 
Click any node from the list and you can see the path to ICOR for it. Alternative path to same ICOR is also mentioned.
However implmentation of second shortest path to nearest ICOR is also implemented. Just comment [Line 61](https://github.com/DaBaap/Network_topology/blob/1f0838d00f5ca5f229ff9cb7f5bde9f50eb8fba6/network_topology/topology/views.py#L61) and uncomment [Line 62](https://github.com/DaBaap/Network_topology/blob/1f0838d00f5ca5f229ff9cb7f5bde9f50eb8fba6/network_topology/topology/views.py#L62) in view.py.

### Path through search bar
In the web page you can see the search bar. Type any node and you can see the suggestion. Click any suggestion or type the node name then press Enter. A path to ICOR should be presented.
If you turn on the toggle for "Search By IP Address" the you can search it via IP Address and **click the suggested node** and then press Enter. 

Note: The images of the nodes are not selected since it was none could be found in SVG within time. 
