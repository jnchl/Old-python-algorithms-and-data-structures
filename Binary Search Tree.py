class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node is None:
            return None

        if key == node.key:
            return node.value
        elif key < node.key:
            if node.left_child is None:
                return None
            else:
                return self.search(key, node.left_child)
        elif key > node.key:
            if node.right_child is None:
                return None
            else:
                return self.search(key, node.right_child)
        else:
            return None

    def insert(self, key, value, node=None):
        if node is None:
            node = self.root

        if node is None:
            self.root = Node(key, value)
        else:
            if key == node.key:
                node.value = value
            elif key < node.key:
                if node.left_child is None:
                    node.left_child = Node(key, value)
                else:
                    self.insert(key, value, node.left_child)

            elif key > node.key:
                if node.right_child is None:
                    node.right_child = Node(key, value)
                else:
                    self.insert(key, value, node.right_child)
            else:
                return None

    def delete(self, key, node=None, previous_node=None):
        if node is None:
            node = self.root
            previous_node = self.root

        if node is None:
            return None

        if key == node.key:
            if node.left_child is None and node.right_child is None:

                if id(node) == id(previous_node):
                    self.root = None

                if previous_node.left_child is not None:
                    if previous_node.left_child.key == key:
                        previous_node.left_child = None

                if previous_node.right_child is not None:
                    if previous_node.right_child.key == key:
                        previous_node.right_child = None


            elif node.left_child is not None and node.right_child is None:

                if id(node) == id(previous_node):
                    self.root = self.root.left_child

                if previous_node.left_child is not None:
                    if previous_node.left_child.key == key:
                        previous_node.left_child = node.left_child

                if previous_node.right_child is not None:
                    if previous_node.right_child.key == key:
                        previous_node.right_child = node.left_child


            elif node.left_child is None and node.right_child is not None:

                if id(node) == id(previous_node):
                    self.root = self.root.right_child

                if previous_node.left_child is not None:
                    if previous_node.left_child.key == key:
                        previous_node.left_child = node.right_child

                if previous_node.right_child is not None:
                    if previous_node.right_child.key == key:
                        previous_node.right_child = node.right_child


            elif node.left_child is not None and node.right_child is not None:

                if id(node) == id(previous_node):

                    succesor_node = node.right_child
                    previous_succesor = succesor_node

                    while succesor_node.left_child is not None:
                        previous_succesor = succesor_node
                        succesor_node = succesor_node.left_child

                    previous_succesor.left_child = succesor_node.right_child

                    root_right_child = self.root.right_child
                    self.root = succesor_node
                    succesor_node.left_child = node.left_child
                    succesor_node.right_child = root_right_child

                else:
                    succesor_node = node.right_child
                    previous_succesor = succesor_node

                    while succesor_node.left_child is not None:
                        previous_succesor = succesor_node
                        succesor_node = succesor_node.left_child

                    previous_succesor.left_child = succesor_node.right_child

                    if previous_node.left_child is not None:
                        if previous_node.left_child.key == key:
                            previous_node.left_child = succesor_node

                    if previous_node.right_child is not None:
                        if previous_node.right_child.key == key:
                            previous_node.right_child = succesor_node

                    succesor_node.left_child = node.left_child


            else:
                return None


        elif key < node.key:
            self.delete(key, node.left_child, node)

        elif key > node.key:
            self.delete(key, node.right_child, node)

        else:
            return None

    def print(self, node):
        if node:
            self.print(node.left_child)
            print('{} {},'.format(node.key, node.value))
            self.print(node.right_child)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right_child, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left_child, lvl + 5)

    def height(self, node=None):
        if node is None:
            return 0

        left_height = self.height(node.left_child)
        right_height = self.height(node.right_child)

        return max(left_height, right_height) + 1


bstest = BST()
key_value_pairs = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K',
                   24: 'L'}

for key in key_value_pairs.keys():
    bstest.insert(key, key_value_pairs[key])

bstest.print_tree()
bstest.print(bstest.root)
print(bstest.search(24))
bstest.insert(20, 'AA')
bstest.insert(6, 'M')
bstest.delete(62)
bstest.insert(59, 'N')
bstest.insert(100, 'P')
bstest.delete(8)
bstest.delete(15)
bstest.insert(55, 'R')
bstest.delete(50)
bstest.delete(5)
bstest.delete(24)
print(bstest.height(bstest.root))
bstest.print(bstest.root)
bstest.print_tree()