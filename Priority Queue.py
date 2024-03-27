class Data_block:
    def __init__(self, priority, dane):
        self.__priority = priority
        self.__dane = dane

    def __lt__(self, other):
        if self.__priority < other.__priority:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__priority > other.__priority:
            return True
        else:
            return False

    def __str__(self):
        return '{} : {}'.format(self.__priority, self.__dane)


class Heap:
    def __init__(self):
        self.tab = []
        self.size = 0

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
            self.tab[dominant_child_index], self.tab[parent_index] = self.tab[parent_index], self.tab[dominant_child_index]
            self.mend_heap(dominant_child_index)

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


heap = Heap()
priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
data = "GRYMOTYLA"

for i in range(len(priorities)):
    heap.enqueue(Data_block(priorities[i], data[i]))

heap.print_tree(0, 0)
heap.print_tab()
first_val = heap.dequeue()
print(heap.peek())
heap.print_tab()
print(first_val)

while heap.size > 0:
    print(heap.dequeue())

heap.print_tab()