import random
import time


class Data_block:
    def __init__(self, priorytet, dane):
        self.__priorytet = priorytet
        self.__dane = dane

    def __lt__(self, other):
        if self.__priorytet < other.__priorytet:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__priorytet > other.__priorytet:
            return True
        else:
            return False

    def __str__(self):
        return '{} : {}'.format(self.__priorytet, self.__dane)


class Heap:
    def __init__(self, tab2sort=None):
        if tab2sort is None:
            self.tab = []
            self.size = 0

        else:
            self.tab = tab2sort
            self.size = len(self.tab)
            last_parent_index = self.parent(len(self.tab))
            while last_parent_index != 0:
                self.mend_heap(last_parent_index)
                last_parent_index -= 1
                while self.left(last_parent_index) >= len(self.tab) and self.right(last_parent_index) >= len(self.tab):
                    last_parent_index -= 1

            self.mend_heap(0)

    def is_empty(self):
        return True if self.size == 0 else False

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return int((index - 1) // 2)

    def peek(self):
        return self.tab[0]

    def enqueue(self, data_block):

        if len(self.tab) == 0:
            self.tab.append(data_block)
            self.size = 1
            return

        elif self.size < len(self.tab):
            self.tab[-1] = data_block
            self.size += 1

        else:
            self.tab.append(data_block)

        data_block_index = len(self.tab) - 1
        self.size = data_block_index + 1
        parent_index = self.parent(data_block_index)

        while self.tab[parent_index] < self.tab[data_block_index]:
            self.tab[parent_index], self.tab[data_block_index] = self.tab[data_block_index], self.tab[parent_index]

            data_block_index = parent_index
            parent_index = self.parent(data_block_index)

            if data_block_index == 0:
                break

    def dequeue(self):
        if self.is_empty():
            return None

        return_data_block = self.tab[0]
        self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]
        self.size -= 1
        self.mend_heap(0)
        return return_data_block

    def mend_heap(self, parent_index):

        if self.left(parent_index) < self.size:
            left_child_index = self.left(parent_index)
        else:
            left_child_index = None

        if self.right(parent_index) < self.size:
            right_child_index = self.right(parent_index)
        else:
            right_child_index = None

        if left_child_index and right_child_index:
            if self.tab[left_child_index] > self.tab[right_child_index]:
                dominant_child_index = left_child_index
            else:
                dominant_child_index = right_child_index

        elif left_child_index:
            dominant_child_index = left_child_index

        elif right_child_index:
            dominant_child_index = right_child_index

        else:
            return

        if self.tab[dominant_child_index] > self.tab[parent_index]:
            self.tab[dominant_child_index], self.tab[parent_index] = self.tab[parent_index], self.tab[
                dominant_child_index]
            self.mend_heap(dominant_child_index)

    def sort(self):
        while not self.is_empty():
            self.dequeue()

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def swap_sort(table):
    for i in range(len(table)):
        m = table.index(min(table[i:]))
        table[i], table[m] = table[m], table[i]

def shift_sort(table):
    for i in range(len(table)):
        m = table.index(min(table[i:]))
        min_val = table[m]
        table.pop(m)
        table.insert(i, min_val)

