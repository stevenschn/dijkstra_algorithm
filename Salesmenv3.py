# GOAL: write program that lets user give origin and destination and return the shortest route with its value.

# Input is given as list of lists. List is to be read as [origin_node neighboring_node distance]

# First problem: write function that lets user define origin and return an ordered list of lists with all neigboring nodes, with the lowest value first.
#       Subproblem: all information in the input is 'double'. Since [A F 1] provides no additional information to [F A 1]. Hence reduce the input list.

def origin_dict(imported_list):
    """Creating a list of all nodes and a list of all nodes with a dictionary of legs, the outcome format will allow to update each leg with 
            extra information, e.g. speed, time, type of route, etc"""
    nodes_list = []
    node_with_leg_lib = []

    # Loop through all items for given list, list lay-out must always be [node, destination, value], etc
    for item in imported_list:
        origin = item[0]
        destination = item[1]
        value = item[2]
        dest_lib = {destination:{'value' : value}}
        total_lib = [origin, {destination:{'value' : value}}]

        # Use nodes_list as a reference to import the total_lib when the node is not yet in the library
        if [origin] not in nodes_list:
            nodes_list.append([origin])
            node_with_leg_lib.append(total_lib)
        
        # Otherwise it updates the node library with a new found leg
        else:
            node_with_leg_lib[nodes_list.index([origin])][1].update(dest_lib)

    return node_with_leg_lib

def nodes_list(imported_list):
    """ Creating a list of all nodes in a network """
    nodes_list = []

    # Loop through all items from given list
    for item in imported_list:
        origin = item[0]

        if origin not in nodes_list:
            nodes_list.append(origin)

    return nodes_list

def tentative_list(imported_list):
    """Creating a tentative list with all available nodes, giving all nodes the initial distance of infinity.
            This is a library, so when update it will never have two inputs for one node"""
    tentative_nodes_lib = {}

    # Loop through all items in a list to add node with distance infinity
    for item in imported_list:
        node = item[0]
        tentative_node = {node : float('inf')}

        if tentative_node not in tentative_nodes_lib.items():
            tentative_nodes_lib.update(tentative_node)

    return tentative_nodes_lib

def leg_search(imported_list, dep_node):
    """ Creating a dictionary of legs coupled to the appropriate departure node, sorted on distance"""
    nodes_dict = origin_dict(imported_list)
    legs = {}
    sorted_legs = []

    for item in nodes_dict:
        if item[0] == dep_node:
            legs.update(item[1])
            for key, value in legs.items():
                arr_node = key
                value = value['value'] # This could be a variable value when more info on legs would be availabe eg. speed, distance, time, etc
                lib_item = (arr_node, value)
                sorted_legs.append(lib_item)

    # Sort tuples in ascending order based on their 'distance'
    sorted_legs.sort(key = lambda x : x[1])
    return sorted_legs

def route_build(imported_list, start_node, goal_node):
    """ Building the shortest route based on an imported list, start_node and goal_node based on the Dijkstra algoritm """
    dep_node = start_node
    arr_node = ''
    
    # Two libraries with tentative distance, in the code below this will consider which is the shortest route
    tentative_distances = {}
    tentative_temp = {}

    # This library will be updated with a list of 'favorite' nodes for each node, this favorite node is indicative for the preceeding which gives the shortest route 
    favorite_nodes = {}
    
    # Creating a visited node list with for now only the start_node
    vis_nodes = [start_node]

    # Give the start node the value zero in the tentative distance library
    start_node_zero = {start_node : 0}
    tentative_distances = tentative_list(imported_list)
    tentative_distances.update(start_node_zero)
    
    while goal_node not in vis_nodes:
        for k, v in leg_search(imported_list, dep_node):
            arr_node = k
            dist = v
            if (dist + tentative_distances[dep_node]) < (tentative_distances[arr_node]):
                new_dist = dist + tentative_distances[dep_node]
                update = {k:new_dist}
                
                fav_node = {arr_node:dep_node}
                tentative_distances.update(update)
                favorite_nodes.update(fav_node)
        
        tentative_temp = tentative_distances.copy()
        
        for item in vis_nodes:
            tentative_temp.pop(item)
            min_node = min(tentative_temp, key=tentative_distances.get)
            dep_node = min_node
        
        vis_nodes.append(min_node)

    # the_route will be build by tracing back the favorite nodes from the goal node, effectively building the route backwards after finding the shortest distance
    the_route = [goal_node]
   
    while the_route[0] is not start_node:
        trace_back = favorite_nodes[the_route[0]]
        the_route.insert(0, trace_back)
    
    distance = tentative_distances[goal_node]

    return the_route, distance

def Main():
    
    input = [ ['A', 'F', 1], ['A', 'G', 8], ['A', 'B', 3], ['B', 'A', 3], ['B', 'C', 4], ['B', 'D', 1], ['B', 'F', 1], ['B', 'G', 6], ['C', 'B', 4], ['C', 'D', 1], ['C', 'E', 2], ['D', 'B', 1], ['D', 'C', 1], ['D', 'E', 5], ['E', 'C', 2], ['E', 'D', 5], [ 'F', 'A', 1], ['F', 'B', 1], ['G', 'A', 8], ['G', 'B', 6]  ]
    #input = [ ['A', 'B', 4],['A', 'C', 3],['A', 'E', 7], ['B', 'A', 4],['B', 'C', 6],['B', 'D', 5], ['C', 'A', 3], ['C', 'B', 6], ['C', 'D', 11], ['C', 'E', 8],['D', 'B', 5],['D', 'C', 11],['D', 'E', 2],['D', 'G', 10],['D', 'F', 2],  ['E', 'A', 7], ['E', 'C', 8], ['E', 'D', 2], ['E', 'G', 5],  ['F', 'D', 2], ['F', 'G', 3], ['G', 'D', 10],['G', 'E', 5],['G', 'F', 3] ]

    # Creating a copy of the original list, so we never modify the original input list
    all_legs = input[:]

    # User input fields
    start_node = 'A'
    goal_node = 'E'
    # End of user input



    result = route_build(all_legs, start_node, goal_node)

    # print("Take the shortest route from " + result[0][0] + " via " + (", ".join(result[0][1:(len(result[0])-1)])) + " to "  + result[0][-1] + ", the distance will be " + str(result[1]) + ".")



