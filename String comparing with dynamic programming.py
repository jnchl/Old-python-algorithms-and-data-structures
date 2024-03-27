import numpy as np
def rec_path(parents):
    i, j = parents.shape
    i-=1
    j-=1
    ret_string = ''
    parent = parents[i][j]

    while parent != 'X':
        ret_string += parent
        if parent == 'D':
            i -= 1

        elif parent == 'I':
            j -= 1

        else:
            i -= 1
            j -= 1

        parent = parents[i][j]

    return ret_string[::-1]

def string_compare_PD(P, T, i=None, j=None):
    if i is None or j is None:
        i = len(P) - 1
        j = len(T) - 1

    D = np.zeros((i + 1, j + 1))
    D[0, :] = np.array([row_it for row_it in range(j + 1)])
    D[:, 0] = np.array([col_it for col_it in range(i + 1)])

    parents = np.array([['X' for row_it in range(j + 1)] for col_it in range(i + 1)])
    parents[0, 1:] = 'I'
    parents[1:, 0] = 'D'

    lut = {0: 'S', 1: 'I', 2: 'D', 3: 'M'}

    for I in range(1, i + 1):
        for J in range(1, j + 1):
            replacements = D[I - 1, J - 1] + (0 if P[I] == T[J] else 1)
            insertions = D[I, J - 1] + 1
            deletions = D[I - 1, J] + 1

            op = np.array([replacements, insertions, deletions])

            if P[I] == T[J]:
                min_index = 3
                min_val = op[np.argmin(op)]
            else:
                min_index = np.argmin(op)
                min_val = op[min_index]

            D[I, J] = min_val
            parents[I, J] = lut[min_index]
    path = rec_path(parents)
    D = D.astype(int)
    return D[-1, -1], D, parents, path

print(string_compare_PD(' biały autobus', ' czarny autokar')[0])