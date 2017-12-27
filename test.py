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
trainMap.routeDistance('A-B-C')
trainMap.routeDistance('A-D')
trainMap.routeDistance('A-D-C')
trainMap.routeDistance('A-E-B-C-D')
trainMap.routeDistance('A-E-D')

trainMap.possibleRoutes('C', 'C', 3, '<=')
trainMap.possibleRoutes('A', 'C', 4, '=')

trainMap.shortestRoute('A', 'C')
trainMap.shortestRoute('B', 'B')

trainMap.possibleRoutesDistance('C', 'C', 30, '<')
