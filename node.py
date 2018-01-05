"""
Definition of the Node Class
"""
class Node:
    """
    Custom Node Class
    """
    def __init__(self, name):
        """
        Constructor for Node objects.
        Initialize node's name to :param name & connected_to to empty dictionary
        :param name: name of node object
        :attribute name: name of node object
        :attribute connected_to: dictionary of neighbor nodes where key is
        Node object and value is edge weight
        """
        self.name = name
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        """
        Adds neighbor node to this node's connected_to dictionary
        :param neighbor: neighbor node object
        :param weight: optional weight of edge to neighbor (defaults to 0)
        """
        self.connected_to[neighbor] = int(weight)

    def get_connections(self):
        """
        Return a list of node objects that are neighbors to this node
        """
        return self.connected_to.keys()

    def get_weight(self, neighbor):
        """
        Return the edge weight to the neighbor of this node object
        :param neighbor: adjacent node object to current node
        """
        return self.connected_to[neighbor]
