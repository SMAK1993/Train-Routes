class Node:
    def __init__(self,name):
        """
        Constructor for Node objects.
        Initialize node's name to :param name & connectedTo to empty dictionary
        :param name: name of node object
        :attribute name: name of node object
        :attribute connectedTo: dictionary of neighbor nodes where key is
        Node object and value is edge weight
        """
        self.name = name
        self.connectedTo = {}

    def addNeighbor(self,neighbor,weight=0):
        """
        Adds neighbor node to this node's connectedTo dictionary
        :param neighbor: neighbor node object
        :param weight: optional weight of edge to neighbor (defaults to 0)
        """
        self.connectedTo[neighbor] = int(weight)

    def getConnections(self):
        """
        Return a list of node objects that are neighbors to this node
        """
        return self.connectedTo.keys()

    def getWeight(self,neighbor):
        """
        Return the edge weight to the neighbor of this node object
        :param neighbor: adjacent node object to current node
        """
        return self.connectedTo[neighbor]
