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

class Edge:
    def __init__(self, capacity, isResidual = False):
        self.capacity = capacity
        self.isResidual = isResidual
        if not isResidual:
            self.residual = capacity
            self.flow = 0
        else:
            self.residual = 0
            self.flow = None

    def __repr__(self):
        return "{} {} {} {}".format(self.capacity, self.flow, self.residual, self.isResidual)


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

    def insertEdge(self, vertex1, vertex2, edge):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)
        vertex1_index = self.index_lookup[vertex1]
        if vertex2 not in self.adjacency_list[vertex1_index]:
            self.adjacency_list[vertex1_index][vertex2] = []
        self.adjacency_list[vertex1_index][vertex2].append(edge)



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
        for neighbour, edge in self.adjacency_list[vertex_idx].items():
            neigbours_list.append((neighbour, edge))
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

def BFS(graph: List_Graph, start_index):
    n = graph.order()
    visited = [0 for i in range(n)]
    parents = [None for i in range(n)]
    queue = []

    queue.append(start_index)
    visited[start_index] = 1

    while queue:
        vertex_index = queue.pop(0)
        neigbours = graph.neighboursIdx(vertex_index)

        for neighbour in neigbours:
            neighbour_index = neighbour[0]
            edges = neighbour[1]

            for edge in edges:
                if visited[neighbour_index] == 0 and edge.residual > 0:
                    queue.append(neighbour_index)
                    visited[neighbour_index] = 1
                    parents[neighbour_index] = vertex_index
                    break



    return parents, visited

def path_analysis(graph: List_Graph, start_index, end_index, parents):
    current_vertex_index = end_index
    lowest_capacity = INF

    if parents[current_vertex_index] is None:
        return 0

    while current_vertex_index != start_index:
        parent_index = parents[current_vertex_index]
        parent_neighours = graph.neighboursIdx(parent_index)

        for parent_neighbour in parent_neighours:
            parent_neighbour_index = parent_neighbour[0]
            parent_neighbour_edges = parent_neighbour[1]

            for parent_neighbour_edge in parent_neighbour_edges:
                if parent_neighbour_index == current_vertex_index and parent_neighbour_edge.isResidual == False:
                    if parent_neighbour_edge.residual < lowest_capacity:
                        lowest_capacity = parent_neighbour_edge.residual
                    new_vertex_index = parent_index

        current_vertex_index = new_vertex_index

    return lowest_capacity

def path_augment(graph: List_Graph, start_index, end_index, parents, lowest_capacity):
    current_vertex_index = end_index

    if parents[current_vertex_index] is None:
        return 0

    while current_vertex_index != start_index:
        parent_index = parents[current_vertex_index]
        parent_neighours = graph.neighboursIdx(parent_index)

        for parent_neighbour in parent_neighours:
            parent_neighbour_index= parent_neighbour[0]
            parent_neighbour_edges = parent_neighbour[1]

            if parent_neighbour_index == current_vertex_index:

                for parent_neighbour_edge in parent_neighbour_edges:
                    if not parent_neighbour_edge.isResidual:
                        parent_neighbour_edge.flow += lowest_capacity
                        parent_neighbour_edge.residual -= lowest_capacity

                    current_vertex_neighbours = graph.neighboursIdx(current_vertex_index)
                    for current_vertex_neighbour in current_vertex_neighbours:
                        current_vertex_neighbour_index = current_vertex_neighbour[0]
                        current_vertex_neighbour_edge = current_vertex_neighbour[1]

                        if current_vertex_neighbour_index == parent_neighbour_index:
                            if current_vertex_neighbour_edge.isResidual:
                                current_vertex_neighbour_edge.residual += lowest_capacity


        current_vertex_index = parent_index

def ford_fulkerson(graph, start_index, end_index):
    parents, visited = BFS(graph, start_index)
    flow = 0

    if visited[end_index] == 0:
        return None

    lowest_capacity = path_analysis(graph, start_index, end_index, parents)

    flow += lowest_capacity

    while lowest_capacity > 0:
        path_augment(graph, start_index, end_index, parents, lowest_capacity)
        parents, visited = BFS(graph, start_index)

        lowest_capacity = path_analysis(graph, start_index, end_index, parents)
        flow += lowest_capacity

    return flow


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


graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
graph = List_Graph()

for ed in graf_0:
    graph.insertEdge(ed[0], ed[1], Edge(ed[2]))
    graph.insertEdge(ed[1], ed[0], Edge(ed[2], isResidual=True))

print(ford_fulkerson(graph, 0, 3))
printGraph(graph)


graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
graph1 = List_Graph()

for ed in graf_1:
    graph1.insertEdge(ed[0], ed[1], Edge(ed[2]))
    graph1.insertEdge(ed[1], ed[0], Edge(ed[2], isResidual=True))

print(ford_fulkerson(graph1, 0, 4))
printGraph(graph1)


graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graph2 = List_Graph()
for ed in graf_2:
    graph2.insertEdge(ed[0], ed[1], Edge(ed[2]))
    graph2.insertEdge(ed[1], ed[0], Edge(ed[2], isResidual=True))

print(ford_fulkerson(graph2, 0, 6))
printGraph(graph2)


graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
graph3 = List_Graph()
for ed in graf_3:
    graph3.insertEdge(ed[0], ed[1], Edge(ed[2]))
    graph3.insertEdge(ed[1], ed[0], Edge(ed[2], isResidual=True))

print(ford_fulkerson(graph3, 0, 4))
printGraph(graph3)