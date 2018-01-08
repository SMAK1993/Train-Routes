# Train-Routes

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: If no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!
For example: The distance of the route A-B-C.
Output: 9

Test Input:

For the test input, the towns are named using the first few letters of the alphabet from A to D.  A route between two towns (A to B) with a distance of 5 is represented as AB5.

Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

**Setup & Running Instructions**
Assuming that either version of Python (2 or 3) are installed and added to path to run solution.

1. Download or clone the repo.
2. Open terminal on MacOS/Linux or powershell on Windows
3. Change directory to Train-Routes
4. Type **python main.py** and hit enter to run the solution

**Change the input data in the main.py file to the input of your choice:**

TOWN_NODES = ['A', 'B', 'C', 'D', 'E']

ROUTE_EDGES = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']

**Use the following methods of the Graph class to compute solutions (Change parameters based on your test cases):**

routeDistance(route)

possibleRoutes(startTown, endTown, maxStops, comparison)

shortestRoute(startTown, endTown)

possibleRoutesDistance(startTown, endTown, distance, comparison)

The solution to the following test can be obtained by running **python test.py**:

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

The following table represents the code coverage of **test.py**:

Name       Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------
graph.py     139      2     78      9    95%   48, 50, 
                                               47->48, 
                                               49->50, 
                                               61->exit, 
                                               95->97, 
                                               174->176, 
                                               197->194, 
                                               219->216, 
                                               241->238, 
                                               280->276
node.py       10      0      0      0   100%
test.py       38      0     10      0   100%
------------------------------------------------------
TOTAL        187      2     88      9    96%
