import numpy as np


# Function that creates matrix for knapsack problem
def kp_matrix(capacity, weights, values):
    item_amount = len(weights)

    matrix = np.zeros((item_amount + 1, capacity + 1))

    for item_it in range(1, item_amount + 1):
        item_weight = weights[item_it - 1]
        item_value = values[item_it - 1]

        for capacity_it in range(1, capacity + 1):
            val_above = matrix[item_it - 1, capacity_it]

            # Assumption that an element won't be assigned
            matrix[item_it, capacity_it] = val_above


            # Check if it's better to assign an element
            if capacity_it >= item_weight and matrix[item_it - 1, capacity_it - item_weight] + item_value > matrix[item_it, capacity_it]:
                matrix[item_it, capacity_it] = matrix[item_it - 1, capacity_it - item_weight] + item_value

    return matrix.astype(int)


# Function that prints elements in the knapsack based on matrix
def kp_elements(matrix, weights, values):
    item_amount = matrix.shape[0] - 1
    capacity = matrix.shape[1] - 1
    item_index_list = []

    current_index = (item_amount, capacity)

    while current_index[0] != 0:
        item_index, current_capacity = current_index
        item_weight = weights[item_index - 1]

        # If there's a change that means that this element is in knapsack
        if matrix[current_index] != matrix[item_index - 1, current_capacity]:
            item_index_list.append(item_index)
            current_index = (item_index - 1, current_capacity - item_weight)
        else:
            current_index = (item_index - 1, current_capacity)


    # knapsack_matrix is a matrix where each column is a one element in the knapsack. First row is the id of the element,
    # second is the value and third is the weight
    knapsack_item_number_list = item_index_list[::-1]

    knapsack_item_index_list = [index - 1 for index in knapsack_item_number_list]
    knapsack_item_value_list = [values[index] for index in knapsack_item_index_list]
    knapsack_item_weight_list = [weights[index] for index in knapsack_item_index_list]

    knapsack_matrix = np.array([knapsack_item_number_list, knapsack_item_value_list, knapsack_item_weight_list], dtype=int)

    return knapsack_matrix


def print_knapsack_problem(values, weights, knapsack_capacity):
    print('Matrix of all elements (Each column is one element) \n Meaning of rows: first = id, second = value, third = weight)')
    all_matrix = np.array([[i for i in range(1, len(values) + 1)], values, weights])
    print(all_matrix)
    print()

    matrix = kp_matrix(knapsack_capacity, weights, values)
    print('Matrix of elements in knapsack (Each column is one element) \n Meaning of rows: first = id, second = value, third = weight)')
    knapsack_element_matrix = kp_elements(matrix, weights, values)
    print(knapsack_element_matrix)
    print()
    print('Total value of elements in knapsack: {}'.format(matrix[-1, -1]))
    print('Total weight of elements in knapsack: {} / {}\n'.format(sum(knapsack_element_matrix[2]), knapsack_capacity))

    print('Matrix of knapsack problem - rows are the elements, columns are the capacities:')
    print(matrix)


values = np.array([2, 2, 4, 5, 3, 2, 1, 6, 2, 4])
weights = np.array([3, 1, 3, 4, 2, 4, 2, 3, 1, 3])

print_knapsack_problem(values, weights, 6)
