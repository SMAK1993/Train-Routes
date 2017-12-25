from graph import Graph
import re

towns = ['A', 'B', 'C', 'D', 'E']
routes = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

trainMap = Graph()

for town in towns:
    trainMap.addNode(town)

for route in routes:
    edge = re.findall('[0-9A-Z][^0-9A-Z]*', route)
    trainMap.addEdge(edge[0], edge[1], edge[2])

trainMap.routeDistance('A-B-C')
trainMap.routeDistance('A-D')
trainMap.routeDistance('A-D-C')
trainMap.routeDistance('A-E-B-C-D')
trainMap.routeDistance('A-E-D')
