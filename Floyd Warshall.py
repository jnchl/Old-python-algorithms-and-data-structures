INF = 999


def floyd_warshall(G):
    V = len(G)

    distance = [[INF for j in range(V)] for i in range(V)]
    prev = [[None for j in range(V)] for i in range(V)]

    for i in range(V):
        for j in range(V):
            distance[i][j] = G[i][j]
            prev[i][j] = i

    for j in range(V):
        distance[j][j] = 0
        prev[j][j] = j

    for k in range(V):
        for i in range(V):
            for j in range(V):

                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    prev[i][j] = prev[k][j]
    return distance, prev


def path_from_floyd_warshall(u, v, prev):
    if prev[u][v] is None:
        return []

    path = [v]

    while u != v:
        v = prev[u][v]
        path.insert(0, v)
    return path


def print_matrix(matrix):
    tempString = ''

    for rowIter in range(len(matrix)):
        tempString += '| '
        for colIter in range(len(matrix[0])):
            if matrix[rowIter][colIter] == INF:
                tempString += "INF" + ' '
            else:
                tempString += str("{0:^3d}".format(matrix[rowIter][colIter])) + ' '

            tempString += '|'
            if rowIter != len(matrix) - 1:
                tempString += '\n'
    return tempString
