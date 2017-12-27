# Train-Routes

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: If no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!
For example: The distance of the route A-B-C.
Output: 9

Test Input:

For the test input, the towns are named using the first few letters of the alphabet from A to D.  A route between two towns (A to B) with a distance of 5 is represented as AB5.

Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

The solution to the following test can be obtained by running python test.py:

1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3 stops.
7. The number of trips starting at A and ending at C with exactly 4 stops.
8. The length of the shortest route (in terms of distance to travel) from A
to C.
9. The length of the shortest route (in terms of distance to travel) from B
to B.
10. The number of different routes from C to C with a distance of less than 30.

**Change the input data in the test.py file:**

towns = ['A', 'B', 'C', 'D', 'E']

routes = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

**Use the following functions of the Graph class to compute solutions:**

Graph.routeDistance(route)

Graph.possibleRoutes(startTown, endTown, maxStops, comparison)

Graph.shortestRoute(startTown, endTown)

Graph.possibleRoutesDistance(startTown, endTown, distance, comparison)
