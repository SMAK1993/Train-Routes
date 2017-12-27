from graph import Graph
import re

"""
List of nodes in the graph
Can contain only 1 uppercase letter (at the beginning)
FORMAT: [Node1, Node2, ..., NodeN]
"""
towns = ['A', 'B', 'C', 'D', 'E']

"""
List of edges in the graph
Nodes must contain only 1 uppercase letter (at the beginning)
FORMAT: Node1Node2Weight
"""
routes = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']


def buildGraph(graph, nodes, edges):
    """
    Build the graph
    :param graph: new Graph object
    :param nodes: list of nodes
    :param edges: list of edges
    """
    for node in nodes:
        graph.addNode(node)
    for edge in edges:
        edge = re.findall('[0-9A-Z][^0-9A-Z]*', edge)
        graph.addEdge(edge[0], edge[1], edge[2])

trainMap = Graph()
buildGraph(trainMap, towns, routes)

"""
routeDistance(route) expects a route in the format Node1-Node2-...-NodeN
"""
trainMap.routeDistance('A-B-C')
trainMap.routeDistance('A-D')
trainMap.routeDistance('A-D-C')
trainMap.routeDistance('A-E-B-C-D')
trainMap.routeDistance('A-E-D')

"""
possibleRoutes(startTown, endTown, maxStops, use 1 of '<' or '<=' or '=')
'<'  means stops LESS THAN maxStops
'<=' means MAXIMUM number of stops is maxStops
'<=' means number of stops is EXACTLY maxStops
"""
trainMap.possibleRoutes('C', 'C', 3, '<=')
trainMap.possibleRoutes('A', 'C', 4, '=')

"""
shortestRoute(startTown, endTown) where startTown & endTown are already in graph
"""
trainMap.shortestRoute('A', 'C')
trainMap.shortestRoute('B', 'B')

"""
possibleRoutesDistance(startTown, endTown, distance, use 1 of '<' or '<=' or '=')
'<'  means distance LESS THAN distance
'<=' means MAXIMUM number of distance is distance
'<=' means number of distance is EXACTLY distance
"""
trainMap.possibleRoutesDistance('C', 'C', 30, '<')
