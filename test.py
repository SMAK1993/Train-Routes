from graph import Graph

graph = Graph()
for i in range(6):
   graph.addNode(i)
print (graph.nodeList)

graph.addEdge(0,1,5)
graph.addEdge(0,5,2)
graph.addEdge(1,2,4)
graph.addEdge(2,3,9)
graph.addEdge(3,4,7)
graph.addEdge(3,5,3)
graph.addEdge(4,0,1)
graph.addEdge(5,4,8)
graph.addEdge(5,2,1)
for node in graph:
   for adjacentNode in node.getConnections():
       print("( %s , %s )" % (node.getName(), adjacentNode.getName()))
