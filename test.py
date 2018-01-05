"""
Importing Regular Expressions & Custom Graph class
"""
import re
from graph import Graph

"""
List of nodes in the graph
Can contain only 1 uppercase letter (at the beginning)
FORMAT: [Node1, Node2, ..., NodeN]
"""
TOWN_NODES = ['A', 'B', 'C', 'D', 'E']

for key, value in enumerate(TOWN_NODES):
    assert isinstance(value, str), "Town index {} with value {} must be of Type String".format(key,value)

"""
List of edges in the graph
Nodes must contain only 1 uppercase letter (at the beginning)
FORMAT: Node1Node2Weight
"""
ROUTE_EDGES = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']


def build_graph(graph, nodes, edges):
    """
    Build the graph
    :param graph: new Graph object
    :param nodes: list of nodes
    :param edges: list of edges
    """
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        edge = re.findall('[0-9A-Z][^0-9A-Z]*', edge)
        graph.add_edge(edge[0], edge[1], edge[2])

TRAIN_MAP = Graph()
build_graph(TRAIN_MAP, TOWN_NODES, ROUTE_EDGES)

"""
route_distance(route) expects a route in the format Node1-Node2-...-NodeN
"""
TRAIN_MAP.route_distance('A-B-C')
TRAIN_MAP.route_distance('A-D')
TRAIN_MAP.route_distance('A-D-C')
TRAIN_MAP.route_distance('A-E-B-C-D')
TRAIN_MAP.route_distance('A-E-D')

"""
possible_routes(startTown, endTown, maxStops, use 1 of '<' or '<=' or '=')
'<'  means stops LESS THAN maxStops
'<=' means MAXIMUM number of stops is maxStops
'<=' means number of stops is EXACTLY maxStops
"""
TRAIN_MAP.possible_routes('C', 'C', 3, '<=')
TRAIN_MAP.possible_routes('A', 'C', 4, '=')

"""
shortest_route(startTown, endTown) where startTown & endTown are already in graph
"""
TRAIN_MAP.shortest_route('A', 'C')
TRAIN_MAP.shortest_route('B', 'B')

"""
possible_routes_distance(startTown, endTown, distance, use 1 of '<' or '<=' or '=')
'<'  means distance LESS THAN distance
'<=' means MAXIMUM number of distance is distance
'<=' means number of distance is EXACTLY distance
"""
TRAIN_MAP.possible_routes_distance('C', 'C', 30, '<')
