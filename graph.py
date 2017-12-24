from node import Node

class Graph:
    def __init__(self):
        self.nodeList = {}
        self.nodeCount = 0

    def addNode(self,name):
        self.nodeCount = self.nodeCount + 1
        newNode = Node(name)
        self.nodeList[name] = newNode
        return newNode

    def getNode(self,name):
        if name in self.nodeList:
            return self.nodeList[name]
        else:
            return None

    def __contains__(self,name):
        return name in self.nodeList

    def addEdge(self,start,end,weight=0):
        if start not in self.nodeList:
            nv = self.addNode(start)
        if end not in self.nodeList:
            nv = self.addNode(end)
        self.nodeList[start].addNeighbor(self.nodeList[end], weight)

    def getNodes(self):
        return self.nodeList.keys()

    def __iter__(self):
        return iter(self.nodeList.values())
