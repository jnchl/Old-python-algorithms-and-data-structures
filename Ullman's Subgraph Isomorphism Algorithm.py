import copy

import numpy as np


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

    def deg(self, vertex_idx):
        degree = 0
        edges_row = self.adjacency_matrix[vertex_idx]
        for weight in edges_row:
            if weight != self.default_value:
                degree += 1

        column = [row[vertex_idx] for row in self.adjacency_matrix]

        for weight in column:
            if weight != self.default_value:
                degree += 1

        return degree

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


def ullman(current_row, M, p_matrix, g_matrix, correct, used_cols=None, no_recursion=0):
    row_amount = M.shape[0]
    col_amount = M.shape[1]

    no_recursion += 1

    if used_cols is None:
        used_cols = [False for i in range(col_amount)]

    if current_row == row_amount:
        MG = M @ g_matrix
        MGT = np.transpose(MG)
        MMGT = M @ MGT

        if np.array_equal(p_matrix, MMGT):
            correct.append(copy.deepcopy(M))

        return no_recursion

    for col_it in range(col_amount):
        if used_cols[col_it] is False:
            used_cols[col_it] = True
            M[current_row] = [0 for i in range(col_amount)]
            M[current_row, col_it] = 1
            no_recursion = ullman(current_row + 1, M, p_matrix, g_matrix, correct, used_cols, no_recursion)
            used_cols[col_it] = False
    return no_recursion


def get_m0(graph: Matrix_Graph, other_graph: Matrix_Graph):
    graph_order, other_graph_order = graph.order(), other_graph.order()

    m0 = np.zeros((graph_order, other_graph_order))

    for row_it in range(graph_order):
        for col_it in range(other_graph_order):
            if graph.deg(row_it) <= other_graph.deg(col_it):
                m0[row_it, col_it] = 1
    return m0


def ullman2(current_row, M, M0, p_matrix, g_matrix, correct, used_cols=None, no_recursion=0):
    row_amount = M.shape[0]
    col_amount = M.shape[1]

    no_recursion += 1

    if used_cols is None:
        used_cols = [False for i in range(col_amount)]

    if current_row == row_amount:
        MG = M @ g_matrix
        MGT = np.transpose(MG)
        MMGT = M @ MGT

        if np.array_equal(p_matrix, MMGT):
            correct.append(copy.deepcopy(M))

        return no_recursion

    for col_it in range(col_amount):
        if used_cols[col_it] is False and M0[current_row, col_it] == 1:
            used_cols[col_it] = True
            M[current_row] = [0 for i in range(col_amount)]
            M[current_row, col_it] = 1
            no_recursion = ullman2(current_row + 1, M, M0, p_matrix, g_matrix, correct, used_cols, no_recursion)
            used_cols[col_it] = False
    return no_recursion


def prune(graph: Matrix_Graph, other_graph: Matrix_Graph, m):
    graph_order, other_graph_order = graph.order(), other_graph.order()
    c = False
    for row_it in range(graph_order):
        for col_it in range(other_graph_order):

            if m[row_it, col_it] != 1:
                continue

            graph_neighbours_idx = graph.neighboursIdx(row_it)
            other_graph_neigbours_idx = other_graph.neighboursIdx(col_it)

            for graph_neighbour_idx in graph_neighbours_idx:
                found = False
                for other_graph_neighbour_idx in other_graph_neigbours_idx:
                    if m[graph_neighbour_idx][other_graph_neighbour_idx] == 1:
                        found = True
                        break
                if found:
                    break
                else:
                    m[row_it][col_it] = 0
                    c = True
    if c:
        return True
    else:
        return False


def ullman3(current_row, M, M0, graph: Matrix_Graph, other_graph: Matrix_Graph, correct, used_cols=None,
            no_recursion=0):
    p_matrix = np.array(graph.adjacency_matrix)
    g_matrix = np.array(other_graph.adjacency_matrix)
    row_amount = M.shape[0]
    col_amount = M.shape[1]

    no_recursion += 1

    if used_cols is None:
        used_cols = [False for i in range(col_amount)]

    if current_row == row_amount:
        MG = M @ g_matrix
        MGT = np.transpose(MG)
        MMGT = M @ MGT

        if np.array_equal(p_matrix, MMGT):
            correct.append(copy.deepcopy(M))

        return no_recursion

    m_copy = copy.deepcopy(M)

    m_changed = False
    if current_row == row_amount - 1:
        m_changed = prune(graph, other_graph, m_copy)

    for col_it in range(col_amount):
        if m_changed and current_row != 0:
            break
        if used_cols[col_it] is False and M0[current_row, col_it] == 1:
            used_cols[col_it] = True
            m_copy[current_row] = [0 for i in range(col_amount)]
            m_copy[current_row, col_it] = 1
            no_recursion = ullman3(current_row + 1, m_copy, M0, graph, other_graph, correct, used_cols, no_recursion)
            used_cols[col_it] = False
    return no_recursion


graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

graph_g = Matrix_Graph()
for edge in graph_G:
    graph_g.insertEdge(*edge)
    graph_g.insertEdge(edge[1], edge[0], edge[2])

graph_p = Matrix_Graph()
for edge in graph_P:
    graph_p.insertEdge(*edge)
    graph_p.insertEdge(edge[1], edge[0], edge[2])

np_graph_G = np.array(graph_g.adjacency_matrix)
np_graph_P = np.array(graph_p.adjacency_matrix)

M = np.zeros((graph_p.order(), graph_g.order()))

correct_matricies = []
recursions = ullman(0, M, np_graph_P, np_graph_G, correct_matricies)
isomorphisms = len(correct_matricies)
print(isomorphisms, recursions)

M0 = get_m0(graph_p, graph_g)
M = np.zeros((graph_p.order(), graph_g.order()))

correct_matricies = []
recursions = ullman2(0, M, M0, np_graph_P, np_graph_G, correct_matricies)
isomorphisms = len(correct_matricies)
print(isomorphisms, recursions)

M0 = get_m0(graph_p, graph_g)
M = np.zeros((graph_p.order(), graph_g.order()))

correct_matricies = []
recursions = ullman3(0, M, M0, graph_p, graph_g, correct_matricies)
isomorphisms = len(correct_matricies)
print(isomorphisms, recursions)