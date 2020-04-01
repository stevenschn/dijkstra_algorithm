def unique_nodes(graph: list):
    unique_nodes = []

    for node in graph:
        if node[0] not in unique_nodes:
            unique_nodes.append(node[0])
        elif node[1] not in unique_nodes:
            unique_nodes.append(node[1])
        else:
            continue
    return unique_nodes

def nodes_dict(nodes_list: list):
    nodes_dict = {}

    for node in nodes_list:
        nodes_dict[node] = [999,[]]
    return nodes_dict

def ordered_neighbors(node: str, graph: list):
    neighbors = []

    for i in range(0,len(graph)):

        if graph[i][0] == node:
            neighbors.append([graph[i][1], graph[i][2]])

    neighbors.sort(key = lambda x: x[1])
    return neighbors

def print_info(route_dis: tuple):
    print('The shortest route is %s which has a total cost of %d.' %(route_dis[0], route_dis[1]))

def route_algoritm(start: str, end: str, graph: list):
    '''Function that uses Dijkstra algorithm to find route '''
    nodes = unique_nodes(graph)
    unvisited_nodes = nodes_dict(nodes)
    visited_nodes = {}

    unvisited_nodes[start][0]=0
    unvisited_nodes[start][1]=start
    
    while True:
        
        # Check if end node is visited, if so: algorithm is finished.
        if end in visited_nodes:
            distance = visited_nodes[end][0]
            route = visited_nodes[end][1]
            return (route, distance)

        # Consider the node with the lowest cost first and find its neighbors with their corresponding costs. 
        # Then add the current node to the visited dictionary.
        current_node = min(unvisited_nodes.items(), key=lambda x: x[1])[0]
        neighbors = ordered_neighbors(current_node, graph)
        visited_nodes[current_node]=unvisited_nodes[current_node]
        del unvisited_nodes[current_node]

        for neighbor in neighbors:
            if neighbor[0] in unvisited_nodes:
                # We add the neighbor of the current node to the visited dict and delete it from the unvisited dict
                first_length = visited_nodes[current_node][0] + neighbor[1]
                
                if first_length < unvisited_nodes[neighbor[0]][0]:
                    unvisited_nodes[neighbor[0]][0] = first_length
                    unvisited_nodes[neighbor[0]][1] = visited_nodes[current_node][1] + neighbor[0]                   

                visited_nodes[neighbor[0]] = unvisited_nodes[neighbor[0]]
                del unvisited_nodes[neighbor[0]]

                # We check the neighbors of the neighbor (which we do not visit yet!)
                new_neighbors = ordered_neighbors(neighbor[0], graph)

                for new_neighbor in new_neighbors:

                    if new_neighbor[0] in unvisited_nodes:

                        second_length = new_neighbor[1]
                        total_length = visited_nodes[neighbor[0]][0] + second_length
                        
                        # We check if the current route is shorter than the one already in the dictionary.
                        if total_length < unvisited_nodes[new_neighbor[0]][0]:
                            unvisited_nodes[new_neighbor[0]][0] = total_length
                            unvisited_nodes[new_neighbor[0]][1] = visited_nodes[neighbor[0]][1] + new_neighbor[0]

# graph = [ ['A', 'B', 4],['A', 'C', 3],['A', 'E', 7], ['B', 'A', 4],['B', 'C', 6],['B', 'D', 5], ['C', 'A', 3], ['C', 'B', 6], ['C', 'D', 11], ['C', 'E', 8],['D', 'B', 5],['D', 'C', 11],['D', 'E', 2],['D', 'G', 10],['D', 'F', 2],  ['E', 'A', 7], ['E', 'C', 8], ['E', 'D', 2], ['E', 'G', 5],  ['F', 'D', 2], ['F', 'G', 3], ['G', 'D', 10],['G', 'E', 5],['G', 'F', 3] ]
graph = [ ['A', 'F', 1], ['A', 'G', 8], ['A', 'B', 3], ['B', 'A', 3], ['B', 'C', 4], ['B', 'D', 1], ['B', 'F', 1], ['B', 'G', 6], ['C', 'B', 4], ['C', 'D', 1], ['C', 'E', 2], ['D', 'B', 1], ['D', 'C', 1], ['D', 'E', 5], ['E', 'C', 2], ['E', 'D', 5], [ 'F', 'A', 1], ['F', 'B', 1], ['G', 'A', 8], ['G', 'B', 6]  ]

(route, distance) = route_algoritm('A', 'E', graph)
print_info((route,distance))

