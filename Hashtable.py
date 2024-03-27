def hashFun(key, tabSize):
    number = None

    if isinstance(key, int):
        number = key
    elif isinstance(key, str):
        sum = 0
        for char in key:
            sum += ord(char)
        number = sum
    else:
        return None

    return int(number % tabSize)


class DataBlock:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def search(self, key):
        index = hashFun(key, len(self.tab))

        if self.tab[index] is not None and self.tab[index].key == key:
            return self.tab[index].value
        else:
            for j in range(len(self.tab)):
                newIndex = (index + self.c2 * j ** 2 + self.c1 * j) % len(self.tab)
                if self.tab[newIndex] is None:
                    continue
                elif self.tab[newIndex].key == key:
                    return self.tab[newIndex].value
                else:
                    continue
        return None


    def insert(self, key, value):
        index = hashFun(key, len(self.tab))
        found = False

        if self.tab[index] is None or self.tab[index].key == key:
            self.tab[index] = DataBlock(key, value)
        else:
            for j in range(len(self.tab)):
                newIndex = (index + self.c2 * j ** 2 + self.c1 * j) % len(self.tab)
                if self.tab[newIndex] is None or self.tab[newIndex].key == key:
                    self.tab[newIndex] = DataBlock(key, value)
                    found = True
                    break;
            if not found:
                print("Out of space")


    def remove(self, key):
        index = hashFun(key, len(self.tab))
        found = False

        if self.tab[index] is None or self.tab[index].key == key:
            self.tab[index] = None
        else:
            for j in range(len(self.tab)):
                newIndex = (index + self.c2 * j ** 2 + self.c1 * j) % len(self.tab)
                if self.tab[newIndex] is None or self.tab[newIndex].key == key:
                    self.tab[newIndex] = None
                    found = True
                    break;
            if not found:
                print("No such key")

    def __str__(self):
        returnString = "{"
        for index in range(len(self.tab)):
            strLine = ""
            if self.tab[index] is None:
                strLine = "None"
            else:
                strLine = "{}:{}".format(self.tab[index].key, self.tab[index].value)
            if index != len(self.tab) - 1:
                strLine += ', '
            returnString += strLine
        returnString += "}"
        return returnString


def firstTest(keys, values, c1, c2):
    hashList = HashTable(13, c1, c2)

    for i in range(15):
        hashList.insert(keys[i], values[i])

    print(hashList)
    print(hashList.search(5))
    print(hashList.search(14))
    hashList.insert(5, 'Z')
    print(hashList.search(5))
    hashList.remove(5)
    print(hashList)
    print(hashList.search(31))
    hashList.insert("test", "W")
    print(hashList)


def secondTest(values, c1, c2):
    hashList = HashTable(13, c1, c2)

    for i in range(15):
        hashList.insert(13 + (13 * i), values[i])

    print(hashList)


keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

firstTest(keys, values, 1, 0)
secondTest(values, 1, 0)

secondTest(values, 0, 1)
firstTest(keys, values, 0, 1)