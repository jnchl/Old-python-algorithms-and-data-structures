import numpy as np


# Funkcja tworząca macierz dla problemu plecakowego
def kp_matrix(capacity, weights, values):
    item_amount = len(weights)
    # Stworzenie macierzy o 1 większej niż potrzeba by pozbyć się problemu out of bounds
    matrix = np.zeros((item_amount + 1, capacity + 1))

    # Iteracja po przedmiotach
    for item_it in range(1, item_amount + 1):
        item_weight = weights[item_it - 1]
        item_value = values[item_it - 1]

        # Iteracja po pojemnościach
        for capacity_it in range(1, capacity + 1):
            val_above = matrix[item_it - 1, capacity_it]

            # Założenie, że nie przydzielamy przedmiotu
            matrix[item_it, capacity_it] = val_above

            # Sprawdzenie czy lepiej przydzielić przedmiot i jeżeli tak to nadpisanie wartości
            if capacity_it >= item_weight and matrix[item_it - 1, capacity_it - item_weight] + item_value > matrix[
                item_it, capacity_it]:
                matrix[item_it, capacity_it] = matrix[item_it - 1, capacity_it - item_weight] + item_value

    return matrix.astype(int)


# Funkcja wypisująca elementy włożone do plecaka na podstawie macierzy
def kp_elements(matrix, weights, values):
    item_amount = matrix.shape[0] - 1
    capacity = matrix.shape[1] - 1
    item_index_list = []

    current_index = (item_amount, capacity)

    # Dopóki funkcja nie przejdzie po wszystkich elementach
    while current_index[0] != 0:
        item_index, current_capacity = current_index
        item_weight = weights[item_index - 1]

        # Jeżeli między wierszami nastąpiła zmiana to przedmiot należy do plecaka i przejście do następnego elementu
        if matrix[current_index] != matrix[item_index - 1, current_capacity]:
            item_index_list.append(item_index)
            current_index = (item_index - 1, current_capacity - item_weight)
        else:
            current_index = (item_index - 1, current_capacity)

    # Stworzenie macierzy gdzie każda kolumna to jeden przedmiot w plecaku, a pierwszy wiersz to numer przedmiotu,
    # drugi wiersz to wartośc przedmiotu, a trzeci wiersz to waga przedmiotu
    knapsack_item_number_list = item_index_list[::-1]

    knapsack_item_index_list = [index - 1 for index in knapsack_item_number_list]
    knapsack_item_value_list = [values[index] for index in knapsack_item_index_list]
    knapsack_item_weight_list = [weights[index] for index in knapsack_item_index_list]

    knapsack_matrix = np.array([knapsack_item_number_list, knapsack_item_value_list, knapsack_item_weight_list], dtype=int)

    return knapsack_matrix


def print_knapsack_problem(values, weights, knapsack_capacity):
    print('Macierz wszystkich elementów (Każda kolumna to jeden przedmiot) \n Znaczenie wierszy: pierwszy = numer przedmiotu, drugi = wartość przedmiotu, trzeci = waga przedmiotu)')
    all_matrix = np.array([[i for i in range(1, len(values) + 1)], values, weights])
    print(all_matrix)
    print()

    matrix = kp_matrix(knapsack_capacity, weights, values)
    print('Macierz elementów w plecaku (Każda kolumna to jeden przedmiot) \n Znaczenie wierszy: pierwszy = numer przedmiotu, drugi = wartość przedmiotu, trzeci = waga przedmiotu)')
    knapsack_element_matrix = kp_elements(matrix, weights, values)
    print(knapsack_element_matrix)
    print()
    print('Całkowita wartość przedmiotów w plecaku: {}'.format(matrix[-1, -1]))
    print('Całkowita waga przedmiotów w plecaku/pojemność plecaka: {} / {}\n'.format(sum(knapsack_element_matrix[2]), knapsack_capacity))

    print('Macierz problemu plecakowego - wiersze to przedmioty, kolumny to pojemności plecaka:')
    print(matrix)


values =  np.array([2, 2, 4, 5, 3, 2, 1, 6, 2, 4])
weights = np.array([3, 1, 3, 4, 2, 4, 2, 3, -1, 3])

print_knapsack_problem(values, weights, 7)
