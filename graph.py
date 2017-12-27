from node import Node
import sys

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

    def possiblePathsMaximum(self, startNode, endNode, maxStops, startedTraversal = False, totalPaths = 0):
        if (maxStops >= 0 and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (maxStops < 0) :
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            totalPaths = totalPaths + self.possiblePathsMaximum(neighbor, endNode, maxStops - 1, startedTraversal)
        return totalPaths

    def possiblePathsExact(self, startNode, endNode, maxStops, startedTraversal = False, totalPaths = 0):
        if (maxStops == 0 and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (maxStops < 0) :
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            totalPaths = totalPaths + self.possiblePathsExact(neighbor, endNode, maxStops - 1, startedTraversal)
        return totalPaths

    def possiblePathsWeighted(self, startNode, endNode, maxWeight, currentWeight = 0, startedTraversal = False, totalPaths = 0):
        if (currentWeight < maxWeight and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (currentWeight >= maxWeight):
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            temp = self.possiblePathsWeighted(neighbor, endNode, maxWeight, currentWeight + startNode.connectedTo[neighbor], startedTraversal, totalPaths)
            if temp:
                totalPaths = temp
        return totalPaths

    def shortestPath(self, startNode, endNode, stops = 0, maxStops = 0, currentWeight = 0, startedTraversal = False, shortestPath = sys.maxsize):
        if not startedTraversal:
            maxStops = self.nodeCount
        if (currentWeight <= shortestPath and startNode == endNode and startedTraversal):
            shortestPath = currentWeight
        if (currentWeight > shortestPath or stops >= maxStops):
            return shortestPath
        for neighbor in startNode.getConnections():
            startedTraversal = True
            stops = stops + 1
            temp = self.shortestPath(neighbor, endNode, stops, maxStops, currentWeight + startNode.connectedTo[neighbor], startedTraversal, shortestPath)
            if temp:
                shortestPath = temp
        return shortestPath
