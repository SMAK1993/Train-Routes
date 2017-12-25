from node import Node
from queue import Queue

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

    def addEdge(self,start,end,weight=0):
        if start not in self.nodeList:
            newNode = self.addNode(start)
        if end not in self.nodeList:
            newNode = self.addNode(end)
        self.nodeList[start].addNeighbor(self.nodeList[end], weight)

    def getNodes(self):
        return self.nodeList.keys()

    def __iter__(self):
        return iter(self.nodeList.values())

    def routeDistance(self, route):
        distance = 0
        routeList = route.split('-')
        for i in range(len(routeList)):
            currentTown = self.getNode(routeList[i])
            if currentTown:
                if i+1 < len(routeList):
                    nextTown = self.getNode(routeList[i+1])
                else:
                    print (distance)
                    return
                if nextTown in currentTown.connectedTo:
                    distance = distance + currentTown.getWeight(nextTown)
                else:
                    print ('NO SUCH ROUTE')
                    return
            else:
                print ('NO SUCH ROUTE')
                return

    def possiblePathsMaximum(self, startNode, endNode, maxStops, startFlag):
        if (maxStops >= 0 and startNode == endNode and startFlag):
            return 1
        if (maxStops <= 0) :
            return 0
        totalPaths = 0
        for neighbor in startNode.getConnections():
            startFlag = True
            totalPaths = totalPaths + self.possiblePathsMaximum(neighbor, endNode, maxStops - 1, startFlag)
        return totalPaths

    def possiblePathsExact(self, startNode, endNode, maxStops, startFlag):
        if (maxStops == 0 and startNode == endNode and startFlag):
            return 1
        if (maxStops <= 0) :
            return 0
        totalPaths = 0
        for neighbor in startNode.getConnections():
            startFlag = True
            totalPaths = totalPaths + self.possiblePathsExact(neighbor, endNode, maxStops - 1, startFlag)
        return totalPaths
