from node import Node
import sys

class Graph:
    def __init__(self):
        """
        Constructor for Graph objects.
        Create graph's dictionary of nodes and set number of nodes to 0
        :attribute nodeList: dictionary of nodes in the graph
        :attribute nodeCount: number of nodes in the graph
        """
        self.nodeList = {}
        self.nodeCount = 0

    def addNode(self,name):
        """
        Create & add node to graph's nodeList dictionary increment nodeCount
        :param name: name of node object being added to graph
        """
        self.nodeCount = self.nodeCount + 1
        newNode = Node(name)
        self.nodeList[name] = newNode
        return newNode

    def getNode(self,name):
        """
        Return the node with :param name from graph's nodeList, else return None
        :param name: name of node object to be returned
        """
        if name in self.nodeList:
            return self.nodeList[name]
        else:
            return None

    def addEdge(self,start,end,weight=0):
        """
        Add end node and weight start node's connectedTo dictionary
        :param start: starting node object where the edge begins
        :param end: ending node object where the edge ends
        :param weight: optional weight of the edge (defaults to 0)
        """
        if start not in self.nodeList:
            newNode = self.addNode(start)
        if end not in self.nodeList:
            newNode = self.addNode(end)
        self.nodeList[start].addNeighbor(self.nodeList[end], weight)

    def routeDistance(self, route):
        """
        Compute & print distance of :param route if it exists, else print
        NO SUCH ROUTE
        :param route: the route to traverse (FORMAT: Node1-Node2-...-NodeN)
        """
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

    def possibleRoutes(self, startTown, endTown, maxStops, comparison):
        """
        Compute & print number of routes from startTown to endTown that meet the
        comparison to maxStops.
        Depending on comparison, a different helper function is called
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxStops: the number of stops to evaluate against
        :param comparison: the comparison operator to use against maxStops
        can be '=' for exact or '<=' for maximum or '<' for less than
        """
        startNode = self.getNode(startTown)
        endNode = self.getNode(endTown)
        if (comparison == "="):
            print (self.possiblePathsExact(startNode, endNode, maxStops))
        elif (comparison == "<="):
            print (self.possiblePathsMaximum(startNode, endNode, maxStops))
        elif (comparison == "<"):
            print (self.possiblePathsLessThan(startNode, endNode, maxStops))

    def possiblePathsLessThan(self, startNode, endNode, maxStops, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown that have edges less than maxStops.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxStops: the number of stops to evaluate against
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with edges less than maxStops
        """
        if (maxStops > 0 and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (maxStops <= 0) :
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            totalPaths = totalPaths + self.possiblePathsLessThan(neighbor, endNode, maxStops - 1, startedTraversal)
        return totalPaths

    def possiblePathsMaximum(self, startNode, endNode, maxStops, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown that have edges less than or equal to maxStops.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxStops: the number of stops to evaluate against
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with edges less than or equal to maxStops
        """
        if (maxStops >= 0 and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (maxStops < 0) :
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            totalPaths = totalPaths + self.possiblePathsMaximum(neighbor, endNode, maxStops - 1, startedTraversal)
        return totalPaths

    def possiblePathsExact(self, startNode, endNode, maxStops, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown have edges equal to maxStops.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxStops: the number of stops to evaluate against
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with edges equal to maxStops
        """
        if (maxStops == 0 and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (maxStops < 0) :
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            totalPaths = totalPaths + self.possiblePathsExact(neighbor, endNode, maxStops - 1, startedTraversal)
        return totalPaths

    def possibleRoutesDistance(self, startTown, endTown, distance, comparison):
        """
        Compute & print number of routes from startTown to endTown that meet the
        comparison to distance.
        Depending on comparison, a different helper function is called
        :param startTown: the starting node
        :param endTown: the ending node
        :param distance: the weight to evaluate against
        :param comparison: the comparison operator to use against distance
        can be '=' for exact or '<=' for maximum or '<' for less than
        """
        startNode = self.getNode(startTown)
        endNode = self.getNode(endTown)
        if (comparison == "="):
            print (self.possiblePathsWeightedExact(startNode, endNode, distance))
        elif (comparison == "<="):
            print (self.possiblePathsWeightedMaximum(startNode, endNode, distance))
        elif (comparison == "<"):
            print (self.possiblePathsWeightedLessThan(startNode, endNode, distance))

    def possiblePathsWeightedLessThan(self, startNode, endNode, maxWeight, currentWeight = 0, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown that have distance less than maxWeight.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxWeight: the weight to evaluate against
        :param currentWeight: the currentWeight of the path so far
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with weight less than maxWeight
        """
        if (currentWeight < maxWeight and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (currentWeight >= maxWeight):
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            temp = self.possiblePathsWeightedLessThan(neighbor, endNode, maxWeight, currentWeight + startNode.connectedTo[neighbor], startedTraversal, totalPaths)
            if temp:
                totalPaths = temp
        return totalPaths

    def possiblePathsWeightedMaximum(self, startNode, endNode, maxWeight, currentWeight = 0, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown that have distance less or equal to maxWeight.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxWeight: the weight to evaluate against
        :param currentWeight: the currentWeight of the path so far
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with weight less or equal to maxWeight
        """
        if (currentWeight < maxWeight and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (currentWeight >= maxWeight):
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            temp = self.possiblePathsWeightedMaximum(neighbor, endNode, maxWeight, currentWeight + startNode.connectedTo[neighbor], startedTraversal, totalPaths)
            if temp:
                totalPaths = temp
        return totalPaths

    def possiblePathsWeightedExact(self, startNode, endNode, maxWeight, currentWeight = 0, startedTraversal = False, totalPaths = 0):
        """
        Recursively compute & return number of routes from
        startTown to endTown that have distance equal to maxWeight.
        :param startTown: the starting node
        :param endTown: the ending node
        :param maxWeight: the weight to evaluate against
        :param currentWeight: the currentWeight of the path so far
        :param startedTraversal: flag for dealing with same start and end
        :param totalPaths: number of routes with weight equal to maxWeight
        """
        if (currentWeight < maxWeight and startNode == endNode and startedTraversal):
            totalPaths = totalPaths + 1
        if (currentWeight >= maxWeight):
            return totalPaths
        for neighbor in startNode.getConnections():
            startedTraversal = True
            temp = self.possiblePathsWeightedExact(neighbor, endNode, maxWeight, currentWeight + startNode.connectedTo[neighbor], startedTraversal, totalPaths)
            if temp:
                totalPaths = temp
        return totalPaths

    def shortestRoute(self, startTown, endTown):
        """
        Compute & print distance of shortest path from startTown to endTown
        :param startTown: the starting node
        :param endTown: the ending node
        """
        startNode = self.getNode(startTown)
        endNode = self.getNode(endTown)
        print (self.shortestPath(startNode, endNode))

    def shortestPath(self, startNode, endNode, stops = 0, maxStops = 0, currentWeight = 0, startedTraversal = False, shortestPath = sys.maxsize):
        """
        Recursively compute & return distance of shortest path
        :param startTown: the starting node
        :param endTown: the ending node
        :param stops: number of stops so far in path
        :param maxStops: the maximum number of stops in the graph
        Initialized to the graphs nodeCount
        :param currentWeight: the currentWeight of the path so far
        :param startedTraversal: flag for dealing with same start and end
        :param shortestPath: the distance of the shortest path
        Initialized to the systems maximum value
        """
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
