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
    assert isinstance(value, str), "Town index {} with value '{}' must be of Type String".format(key, value)
    assert not " " in value, "Town index {} with value '{}' must not contain whitespace".format(key, value)
    assert value[0].isupper(), "Town index {} with value '{}' must begin with uppercase letter".format(key, value)
    number_of_uppercase = sum(1 for letter in value if letter.isupper())
    assert number_of_uppercase == 1, "Town index {} with value '{}' must contain only 1 uppercase letter".format(key, value)

"""
List of edges in the graph
Nodes must contain only 1 uppercase letter (at the beginning)
FORMAT: Node1Node2Weight
"""
ROUTE_EDGES = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

for key, value in enumerate(ROUTE_EDGES):
    assert isinstance(value, str), "Route index {} with value '{}' must be of Type String".format(key, value)
    assert not " " in value, "Route index {} with value '{}' must not contain whitespace".format(key, value)
    route = re.findall('[0-9A-Z][^0-9A-Z]*', value)
    assert len(route) == 3, "Route index {} with value '{}' must contain exactly 2 uppercase letters (the first letter of each town)".format(key, value)

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
assert TRAIN_MAP.route_distance('A-B-C') == 9, "Route Distance 'A-B-C' must be 9"
assert TRAIN_MAP.route_distance('A-D') == 5, "Route Distance 'A-D' must be 5"
assert TRAIN_MAP.route_distance('A-D-C') == 13, "Route Distance 'A-D-C' must be 13"
assert TRAIN_MAP.route_distance('A-E-B-C-D') == 22, "Route Distance 'A-E-B-C-D' must be 22"
assert TRAIN_MAP.route_distance('A-E-D') == 0, "Route Distance 'A-E-D' must be 0"

"""
possible_routes(startTown, endTown, maxStops, use 1 of '<' or '<=' or '=')
'<'  means stops LESS THAN maxStops
'<=' means MAXIMUM number of stops is maxStops
'<=' means number of stops is EXACTLY maxStops
"""
assert TRAIN_MAP.possible_routes('C', 'C', 3, '<=') == 2, "Possible Paths for 'C' to 'C' must be 2"
assert TRAIN_MAP.possible_routes('A', 'C', 4, '=') == 3, "Possible Paths for 'C' to 'C' must be 3"

"""
shortest_route(startTown, endTown) where startTown & endTown are already in graph
"""
assert TRAIN_MAP.shortest_route('A', 'C') == 9, "Shortest Distance for 'A' to 'C' must be 9"
assert TRAIN_MAP.shortest_route('B', 'B') == 9, "Shortest Distance for 'B' to 'B' must be 9"

"""
possible_routes_distance(startTown, endTown, distance, use 1 of '<' or '<=' or '=')
'<'  means distance LESS THAN distance
'<=' means MAXIMUM number of distance is distance
'<=' means number of distance is EXACTLY distance
"""
assert TRAIN_MAP.possible_routes_distance('C', 'C', 30, '<') == 7, "Possible Paths for 'C' to 'C' must be 7"

print("\nCustom Tests to Increase Code Coverage")
TRAIN_MAP.route_distance('F-G')
TRAIN_MAP.possible_routes('A', 'C', 4, '<')
TRAIN_MAP.possible_routes_distance('C', 'C', 30, '<=')
TRAIN_MAP.possible_routes_distance('A', 'C', 9, '=')
