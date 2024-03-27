import numpy as np

def johnson(og_matrix: np.ndarray):
    row_size, col_size = og_matrix.shape
    matrix = og_matrix.copy()
    matrix = matrix.astype(float)
    result_matrix = np.zeros((row_size, col_size))
    left_it = 0
    right_it = col_size - 1

    while left_it <= right_it:
        m_one_min_index = np.nanargmin(matrix[0])
        m_two_min_index = np.nanargmin(matrix[1])
        m_one_min = matrix[0, m_one_min_index]
        m_two_min = matrix[1, m_two_min_index]

        if m_one_min < m_two_min or m_one_min == m_two_min:
            result_matrix[:, left_it] = matrix[:, m_one_min_index]
            matrix[:, m_one_min_index] = np.nan
            left_it += 1

        elif m_two_min < m_one_min:
            result_matrix[:, right_it] = matrix[:, m_two_min_index]
            matrix[:, m_two_min_index] = np.nan
            right_it -= 1
        else:
            raise ValueError
    time_matrix = result_matrix.copy()
    time_matrix[1, 0] = time_matrix[1, 0] + time_matrix[0, 0]
    for j in range(1, col_size):
        time_matrix[0, j] = time_matrix[0, j] + time_matrix[0, j - 1]
        time_matrix[1, j] += max(time_matrix[0, j], time_matrix[1, j-1])
    return result_matrix, time_matrix


matrix = np.array([[9, 6, 8, 7, 12, 3],
[7, 3, 5, 10, 4, 7]])
matrix2 = np.array([[9, 6, 8, 7, 12, 3, 1, 5, 23, 11],
[7, 3, 5, 10, 4, 7, 4, 6, 20, 17]])
m, t = johnson(matrix)

print('Uszeregowanie:')
print(m)
print('\n Długość uszeregowania:')
print(t)
print('\n')
m, t = johnson(matrix2)
print('Uszeregowanie:')
print(m)
print('\n Długość uszeregowania:')
print(t)