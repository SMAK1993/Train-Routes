class Node:
    def __init__(self,name):
        self.name = name
        self.connectedTo = {}

    def addNeighbor(self,neighbor,weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.name) + ' connectedTo: ' + str([node.name for node in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getName(self):
        return self.name

    def getWeight(self,neighbor):
        return self.connectedTo[neighbor]
