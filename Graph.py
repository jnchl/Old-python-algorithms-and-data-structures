class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return True if self.key == other.key else False

    def __hash__(self):
        return hash(self.key)


class Matrix_Graph:
    def __init__(self, default_value=0):
        self.adjacency_matrix = []
        self.vertex_list = []
        self.index_lookup = {}
        self.default_value = default_value

    def isEmpty(self):
        if len(self.vertex_list) == 0:
            return True
        for it in range(len(self.vertex_list)):
            if self.vertex_list[it] is not None:
                return False
        return True

    def update_matrix(self):
        matrix_size = len(self.vertex_list)
        for row_it in range(matrix_size):
            while len(self.adjacency_matrix[row_it]) < matrix_size:
                self.adjacency_matrix[row_it].append(self.default_value)

    def insertVertex(self, vertex):
        self.vertex_list.append(vertex)
        vertex_index = len(self.vertex_list) - 1
        self.index_lookup[vertex] = vertex_index
        self.adjacency_matrix.append([self.default_value for i in range(len(self.vertex_list))])
        self.update_matrix()

    def insertEdge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.vertex_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.vertex_list:
            self.insertVertex(vertex2)
        vertex1_index = self.index_lookup[vertex1]
        vertex2_index = self.index_lookup[vertex2]
        self.adjacency_matrix[vertex1_index][vertex2_index] = weight

    def deleteVertex(self, vertex):
        vertex_index = self.index_lookup[vertex]
        self.vertex_list[vertex_index] = None
        self.index_lookup.pop(vertex)
        self.adjacency_matrix[vertex_index] = [self.default_value for i in range(len(self.vertex_list))]
        for row_it in range(len(self.adjacency_matrix)):
            self.adjacency_matrix[row_it][vertex_index] = self.default_value

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 not in self.vertex_list and vertex2 not in self.vertex_list:
            print('No edge to delete')
        else:
            vertex1_index = self.index_lookup[vertex1]
            vertex2_index = self.index_lookup[vertex2]
            self.adjacency_matrix[vertex1_index][vertex2_index] = self.default_value

    def getVertexIdx(self, vertex):
        if vertex not in self.index_lookup.keys():
            return None
        else:
            return self.index_lookup[vertex]

    def getVertex(self, vertex_idx):
        return self.vertex_list[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        neighbours_list = self.neighbours(vertex_idx)
        return [self.getVertexIdx(neighbour) for neighbour in neighbours_list]

    def neighbours(self, vertex_idx):
        neighbours_list = []
        for vertex_it in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[vertex_idx][vertex_it] != self.default_value:
                neighbours_list.append(self.getVertex(vertex_it))
        return neighbours_list

    def order(self):
        vertex_amount = 0
        for it in range(len(self.vertex_list)):
            if self.vertex_list[it] is not None:
                vertex_amount += 1
        return vertex_amount

    def size(self):
        size = 0
        matrix_size = len(self.adjacency_matrix)
        for row_it in range(matrix_size):
            for col_it in range(matrix_size):
                if self.adjacency_matrix[row_it][col_it] != self.default_value:
                    size += 1
        return size

    def edges(self):
        edge_list = []
        for vertex_it in range(len(self.adjacency_matrix)):
            if self.vertex_list[vertex_it] is not None:
                for vertex_it_2 in range(len(self.adjacency_matrix)):
                    if self.vertex_list[vertex_it_2] is not None:
                        if self.adjacency_matrix[vertex_it][vertex_it_2] != self.default_value:
                            edge_list.append((self.getVertex(vertex_it), self.getVertex(vertex_it_2)))
        return edge_list


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
        return [self.getVertexIdx(neighbour) for neighbour in neighbours]

    def neighbours(self, vertex_idx):
        return self.adjacency_list[vertex_idx].keys()

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