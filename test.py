from graph import Graph
import re

towns = ['A', 'B', 'C', 'D', 'E']
routes = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

def buildGraph(graph, nodes, edges):
    for node in nodes:
        graph.addNode(node)
    for edge in edges:
        edge = re.findall('[0-9A-Z][^0-9A-Z]*', edge)
        graph.addEdge(edge[0], edge[1], edge[2])

trainMap1 = Graph()
buildGraph(trainMap1, towns, routes)
trainMap1.routeDistance('A-B-C')
trainMap1.routeDistance('A-D')
trainMap1.routeDistance('A-D-C')
trainMap1.routeDistance('A-E-B-C-D')
trainMap1.routeDistance('A-E-D')

trainMap2 = Graph()
buildGraph(trainMap2, towns, routes)
possibleRoutes = trainMap2.possiblePathsMaximum(trainMap2.getNode('C'), trainMap2.getNode('C'), 3, False)
print (possibleRoutes)

trainMap3 = Graph()
buildGraph(trainMap3, towns, routes)
possibleRoutes = trainMap3.possiblePathsExact(trainMap3.getNode('A'), trainMap3.getNode('C'), 4, False)
print (possibleRoutes)
