import math
INF = math.inf

def nearest_neighbour(G, start):
    path = [start]

    visited = [start]
    graph_size = len(G)
    cost = 0

    for i in range(graph_size - 1):
        previous_node = path[-1]
        weight_row = G[previous_node]
        weight_row = [float(weight) for weight in weight_row]
        for node in range(len(weight_row)):
            if node in visited:
                weight_row[node] = INF
        minimal_weight = min(weight_row)
        next_node_index = weight_row.index(minimal_weight)

        next_node = next_node_index
        path.append(next_node)
        visited.append(next_node)
        cost += G[previous_node][next_node]

    actual_path = [node + 1 for node in path]
    return actual_path, cost