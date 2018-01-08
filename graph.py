"""
Importing System Library & Custom Node class
"""
import sys
from node import Node

class Graph:
    """
    Custom Graph Class
    """
    def __init__(self):
        """
        Constructor for Graph objects.
        Create graph's dictionary of nodes and set number of nodes to 0\n
        :attribute node_list: dictionary of nodes in the graph\n
        :attribute node_count: number of nodes in the graph\n
        """
        self.node_list = {}
        self.node_count = 0

    def add_node(self, name):
        """
        Create & add node to graph's node_list dictionary increment node_count\n
        :param name: name of node object being added to graph\n
        """
        self.node_count = self.node_count + 1
        new_node = Node(name)
        self.node_list[name] = new_node
        return new_node

    def get_node(self, name):
        """
        Return the node with :param name from graph's node_list, else return None\n
        :param name: name of node object to be returned\n
        """
        if name in self.node_list:
            return self.node_list[name]
        return None

    def add_edge(self, start, end, weight=0):
        """
        Add end node and weight start node's connected_to dictionary\n
        :param start: starting node object where the edge begins\n
        :param end: ending node object where the edge ends\n
        :param weight: optional weight of the edge (defaults to 0)\n
        """
        if start not in self.node_list:
            self.add_node(start)
        if end not in self.node_list:
            self.add_node(end)
        self.node_list[start].add_neighbor(self.node_list[end], weight)

    def route_distance(self, route):
        """
        Compute & print distance of :param route if it exists, else print
        NO SUCH ROUTE\n
        :param route: the route to traverse (FORMAT: Node1-Node2-...-NodeN)\n
        """
        distance = 0
        route_list = route.split('-')
        for key, value in enumerate(route_list):
            current_town = self.get_node(value)
            if current_town:
                if key + 1 < len(route_list):
                    next_town = self.get_node(route_list[key + 1])
                else:
                    print(distance)
                    return distance
                if next_town in current_town.connected_to:
                    distance = distance + current_town.get_weight(next_town)
                else:
                    print('NO SUCH ROUTE')
                    return 0
            else:
                print('NO SUCH ROUTE')
                return 0

    def possible_routes(self, start_town, end_town, max_stops, comparison):
        """
        Compute & print number of routes from start_town to end_town that meet the
        comparison to max_stops.\n
        Depending on comparison, a different helper function is called.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_stops: the number of stops to evaluate against\n
        :param comparison: the comparison operator to use against max_stops
        can be '=' for exact or '<=' for maximum or '<' for less than\n
        """
        start_node = self.get_node(start_town)
        end_node = self.get_node(end_town)
        if comparison == "=":
            result = self.possible_paths_exact(start_node, end_node, max_stops)
        elif comparison == "<=":
            result = self.possible_paths_maximum(start_node, end_node, max_stops)
        elif comparison == "<":
            result = self.possible_paths_less_than(start_node, end_node, max_stops)
        print(result)
        return result

    def possible_paths_less_than(self, start_node, end_node, max_stops, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town that have edges less than max_stops.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_stops: the number of stops to evaluate against\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with edges less than max_stops\n
        """
        if max_stops > 0 and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if max_stops <= 0:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            total_paths = total_paths + self.possible_paths_less_than(neighbor, end_node, max_stops - 1, started_traversal)
        return total_paths

    def possible_paths_maximum(self, start_node, end_node, max_stops, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town that have edges less than or equal to max_stops.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_stops: the number of stops to evaluate against\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with edges less than or equal to max_stops\n
        """
        if max_stops >= 0 and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if max_stops < 0:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            total_paths = total_paths + self.possible_paths_maximum(neighbor, end_node, max_stops - 1, started_traversal)
        return total_paths

    def possible_paths_exact(self, start_node, end_node, max_stops, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town have edges equal to max_stops.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_stops: the number of stops to evaluate against\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with edges equal to max_stops\n
        """
        if max_stops == 0 and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if max_stops < 0:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            total_paths = total_paths + self.possible_paths_exact(neighbor, end_node, max_stops - 1, started_traversal)
        return total_paths

    def possible_routes_distance(self, start_town, end_town, distance, comparison):
        """
        Compute & print number of routes from start_town to end_town that meet the
        comparison to distance.\n
        Depending on comparison, a different helper function is called.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param distance: the weight to evaluate against\n
        :param comparison: the comparison operator to use against distance
        can be '=' for exact or '<=' for maximum or '<' for less than\n
        """
        start_node = self.get_node(start_town)
        end_node = self.get_node(end_town)
        if comparison == "=":
            result = self.possible_paths_weighted_exact(start_node, end_node, distance)
        elif comparison == "<=":
            result = self.possible_paths_weighted_maximum(start_node, end_node, distance)
        elif comparison == "<":
            result = self.possible_paths_weighted_lt(start_node, end_node, distance)
        print(result)
        return result

    def possible_paths_weighted_lt(self, start_node, end_node, max_weight, current_weight=0, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town that have distance less than max_weight.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_weight: the weight to evaluate against\n
        :param current_weight: the current_weight of the path so far\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with weight less than max_weight\n
        """
        if current_weight < max_weight and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if current_weight >= max_weight:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            temp = self.possible_paths_weighted_lt(neighbor, end_node, max_weight, current_weight + start_node.connected_to[neighbor], started_traversal, total_paths)
            if temp:
                total_paths = temp
        return total_paths

    def possible_paths_weighted_maximum(self, start_node, end_node, max_weight, current_weight=0, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town that have distance less or equal to max_weight.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_weight: the weight to evaluate against\n
        :param current_weight: the current_weight of the path so far\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with weight less or equal to max_weight\n
        """
        if current_weight <= max_weight and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if current_weight >= max_weight:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            temp = self.possible_paths_weighted_maximum(neighbor, end_node, max_weight, current_weight + start_node.connected_to[neighbor], started_traversal, total_paths)
            if temp:
                total_paths = temp
        return total_paths

    def possible_paths_weighted_exact(self, start_node, end_node, max_weight, current_weight=0, started_traversal=False, total_paths=0):
        """
        Recursively compute & return number of routes from
        start_town to end_town that have distance equal to max_weight.\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param max_weight: the weight to evaluate against\n
        :param current_weight: the current_weight of the path so far\n
        :param started_traversal: flag for dealing with same start and end\n
        :param total_paths: number of routes with weight equal to max_weight\n
        """
        if current_weight == max_weight and start_node == end_node and started_traversal:
            total_paths = total_paths + 1
        if current_weight >= max_weight:
            return total_paths
        for neighbor in start_node.get_connections():
            started_traversal = True
            temp = self.possible_paths_weighted_exact(neighbor, end_node, max_weight, current_weight + start_node.connected_to[neighbor], started_traversal, total_paths)
            if temp:
                total_paths = temp
        return total_paths

    def shortest_route(self, start_town, end_town):
        """
        Compute & print distance of shortest path from start_town to end_town\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        """
        start_node = self.get_node(start_town)
        end_node = self.get_node(end_town)
        result = self.shortest_path(start_node, end_node)
        print(result)
        return result

    def shortest_path(self, start_node, end_node, stops=0, max_stops=0, current_weight=0, started_traversal=False, shortest_path=sys.maxsize):
        """
        Recursively compute & return distance of shortest path\n
        :param start_town: the starting node\n
        :param end_town: the ending node\n
        :param stops: number of stops so far in path\n
        :param max_stops: the maximum number of stops in the graph\n
        Initialized to the graphs node_count\n
        :param current_weight: the current_weight of the path so far\n
        :param started_traversal: flag for dealing with same start and end\n
        :param shortest_path: the distance of the shortest path
        Initialized to the systems maximum value\n
        """
        if not started_traversal:
            max_stops = self.node_count
        if current_weight <= shortest_path and start_node == end_node and started_traversal:
            shortest_path = current_weight
        if current_weight > shortest_path or stops >= max_stops:
            return shortest_path
        for neighbor in start_node.get_connections():
            started_traversal = True
            stops = stops + 1
            temp = self.shortest_path(neighbor, end_node, stops, max_stops, current_weight + start_node.connected_to[neighbor], started_traversal, shortest_path)
            if temp:
                shortest_path = temp
        return shortest_path
