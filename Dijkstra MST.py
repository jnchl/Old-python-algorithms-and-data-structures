import math

INF = math.inf


class Vertex:
    def __init__(self, key, color=0, brightness=0):
        self.key = key
        self.color = color
        self.brightness = brightness

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __hash__(self):
        return hash(self.key)


class List_Graph:
    def __init__(self):
        self.adjacency_list = []
        self.vertex_list = []
        self.index_lookup = {}

    def isEmpty(self):
        if len(self.vertex_list) == 0:
            return True
        for it in range(len(self.vertex_list)):
            if self.vertex_list[it] is not None:
                return False
        return True

    def insertVertex(self, vertex):
        self.vertex_list.append(vertex)
        vertex_index = len(self.vertex_list) - 1
        self.index_lookup[vertex] = vertex_index
        self.adjacency_list.append({})

    def insertEdge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)
        vertex1_index = self.index_lookup[vertex1]
        self.adjacency_list[vertex1_index][vertex2] = weight

    def deleteVertex(self, vertex):
        vertex_index = self.index_lookup[vertex]
        self.vertex_list[vertex_index] = None
        self.index_lookup.pop(vertex)
        self.adjacency_list[vertex_index] = None
        for it in range(len(self.adjacency_list)):
            if self.adjacency_list[it] is not None:
                for neighbour in list(self.adjacency_list[it].keys()):
                    if neighbour == vertex:
                        del self.adjacency_list[it][neighbour]

    def deleteEdge(self, vertex1, vertex2):
        vertex1_index = self.index_lookup[vertex1]
        if self.adjacency_list[vertex1_index] is not None:
            if self.adjacency_list[vertex1_index] is not None:
                for neighbour in list(self.adjacency_list[vertex1_index].keys()):
                    if neighbour == vertex2:
                        del self.adjacency_list[vertex1_index][neighbour]

    def getVertexIdx(self, vertex):
        if vertex not in self.index_lookup.keys():
            return None
        else:
            return self.index_lookup[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        neighbours = self.neighbours(vertex_idx)
        return [(self.getVertexIdx(neighbour[0]), neighbour[1]) for neighbour in neighbours]

    def neighbours(self, vertex_idx):
        neigbours_list = []
        if self.adjacency_list[vertex_idx] is None:
            return None
        for neighbour, weight in self.adjacency_list[vertex_idx].items():
            neigbours_list.append((neighbour, weight))
        return neigbours_list

    def order(self):
        vertex_amount = 0
        for it in range(len(self.vertex_list)):
            if self.vertex_list[it] is not None:
                vertex_amount += 1
        return vertex_amount

    def size(self):
        size = 0
        for it in range(len(self.adjacency_list)):
            if self.adjacency_list[it] is not None:
                size += len(list(self.adjacency_list[it].keys()))
        return size

    def edges(self):
        edge_list = []
        for it in range(len(self.adjacency_list)):
            if self.vertex_list[it] is not None:
                neighbours = self.adjacency_list[it].keys()
                for neighbour in neighbours:
                    edge_list.append((self.getVertex(it), neighbour))
        return edge_list


def MST(graph: List_Graph):
    ret_graph = List_Graph()
    for vertex in graph.vertex_list:
        ret_graph.insertVertex(vertex)
    n = graph.order()
    intree = [0 for i in range(n)]
    distance = [INF for i in range(n)]
    parent = [-1 for i in range(n)]
    total_weight = 0

    distance[0] = 0
    v = 0

    while intree[v] == 0:
        intree[v] = 1
        if v != 0:
            ret_graph.insertEdge(graph.getVertex(parent[v]), graph.getVertex(v), int(distance[v]))
            ret_graph.insertEdge(graph.getVertex(v), graph.getVertex(parent[v]), int(distance[v]))
            total_weight += int(distance[v])

        neighbours = graph.neighboursIdx(v)
        for edge in neighbours:
            neighbour = edge[0]
            weight = edge[1]

            if distance[neighbour] > weight and intree[neighbour] == 0:
                distance[neighbour] = weight
                parent[neighbour] = v

        v = 0
        dist = INF
        for i in range(n):
            if intree[i] == 0 and dist > distance[i]:
                dist = distance[i]
                v = i

    return ret_graph, total_weight


def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(j, w, end=";")
        print()
    print("-------------------")

graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

graph = List_Graph()


for edge in graf:
    graph.insertEdge(edge[0], edge[1], edge[2])
    graph.insertEdge(edge[1], edge[0], edge[2])

mst, weight = MST(graph)
printGraph(mst)