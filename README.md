# dijkstra_algorithm
python code which implements dijkstra's algorithm for routing

Simple code that finds the shortest route (shortest indexed by 'costs' but could be anything: distance/costs/efficiency/speed) 
with Dijkstra's algorithm. It uses an input of a list of lists. Where each list consists of a two node strings and a cost integer. E.g.

input = [ ['A', 'B', 3], ['B', 'A', 3] , ['B', 'C', 5], ['C', 'B', 5] ] 

It returns a tuple of the form (route, costs), where route is a string of nodes and cost is an integer. Additionaly, a print
function returns the found route and cost.
