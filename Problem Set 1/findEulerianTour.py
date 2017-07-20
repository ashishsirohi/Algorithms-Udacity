# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_degree(graph):
    nodes = find_nodes(graph)
    degree = {}
    connected_nodes = {}
    for n in nodes:
        count = 0
        ll = []
        for x, y in graph:
            if x == n:
                count += 1
                ll.append(y)
            if y == n:
                count += 1
                ll.append(x)
        degree.update({n: count})
        connected_nodes.update({n: ll})
    return degree, connected_nodes


def find_nodes(graph):
    nodes = []
    for x, y in graph:
        if x not in nodes:
            nodes.append(x)
        if y not in nodes:
            nodes.append(y)
    return nodes


def tour_possible(graph):
    degree, connected_nodes = find_degree(graph)
    # print degree
    # print connected_nodes
    odd_degree_nodes = []
    for key in degree:
        if degree[key] % 2 != 0:
            odd_degree_nodes.append(degree[key])

    if len(odd_degree_nodes) == 0 or len(odd_degree_nodes) == 2:
        return odd_degree_nodes
    else:
        return False


def find_eulerian_tour(graph):
    stack = []
    tour = []
    tour_poss = tour_possible(graph)
    nodes = find_nodes(graph)
    degree, connected_nodes = find_degree(graph)
    # print connected_nodes[2]
    if (tour_poss != False):
        if (len(tour_poss) == 2):
            current_node = tour_poss[0]
            stack.append(current_node)
        else:
            current_node = nodes[0]
            stack.append(current_node)

    graph_copy = graph

    while (len(stack) > 0):
        if len(connected_nodes[current_node]) > 0:
            prev_node = current_node
            current_node = connected_nodes[current_node].pop()
            connected_nodes[current_node].remove(prev_node)
            stack.append(current_node)


        else:
            current_node = stack.pop()
            tour.append(current_node)
    print tour
    return []


find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5),
                    (4, 8), (1, 6), (3, 7), (5, 9),
                    (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])