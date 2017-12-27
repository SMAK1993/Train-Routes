class Node:
    def __init__(self,name):
        self.name = name
        self.connectedTo = {}

    def addNeighbor(self,neighbor,weight=0):
        self.connectedTo[neighbor] = int(weight)

    def getConnections(self):
        return self.connectedTo.keys()

    def getName(self):
        return self.name

    def getWeight(self,neighbor):
        return self.connectedTo[neighbor]
