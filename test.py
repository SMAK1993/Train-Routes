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

trainMap = Graph()
buildGraph(trainMap, towns, routes)
trainMap.routeDistance('A-B-C')
trainMap.routeDistance('A-D')
trainMap.routeDistance('A-D-C')
trainMap.routeDistance('A-E-B-C-D')
trainMap.routeDistance('A-E-D')

# possibleRoutes = trainMap.possiblePathsMaximum(trainMap.getNode('C'), trainMap.getNode('C'), 3)
print (trainMap.possiblePathsMaximum(trainMap.getNode('C'), trainMap.getNode('C'), 3))

# possibleRoutes = trainMap.possiblePathsExact(trainMap.getNode('A'), trainMap.getNode('C'), 4)
print (trainMap.possiblePathsExact(trainMap.getNode('A'), trainMap.getNode('C'), 4))

# possibleRoutes = trainMap.possiblePathsExact(trainMap.getNode('A'), trainMap.getNode('C'), 4)
print (trainMap.shortestPath(trainMap.getNode('A'), trainMap.getNode('C')))

# possibleRoutes = trainMap.possiblePathsExact(trainMap.getNode('A'), trainMap.getNode('C'), 4)
print (trainMap.shortestPath(trainMap.getNode('B'), trainMap.getNode('B')))

# possibleRoutes = trainMap.possiblePathsWeighted(trainMap.getNode('C'), trainMap.getNode('C'), 30)
print (trainMap.possiblePathsWeighted(trainMap.getNode('C'), trainMap.getNode('C'), 30))
