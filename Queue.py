def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]

class queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = 0
        self.writeIndex = 0
        self.readIndex = 0

    def is_empty(self):
        return True if self.writeIndex == self.readIndex else False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.readIndex]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.size -= 1
            returnVal = self.tab[self.readIndex]

            if self.readIndex == len(self.tab) - 1:
                self.readIndex = 0
            else:
                self.readIndex += 1
            return returnVal

    def enqueue(self, val):
        oldVal = self.tab[self.writeIndex]
        self.tab[self.writeIndex] = val

        if self.writeIndex == len(self.tab) - 1:
            self.writeIndex = 0
        else:
            self.writeIndex += 1

        if self.writeIndex == self.readIndex:
            oldLen = len(self.tab)
            self.tab = realloc(self.tab, 2 * len(self.tab))
            for i in range(self.readIndex, oldLen):
                self.tab[i + oldLen] = self.tab[i]
                self.tab[i] = None
                self.tab[oldLen] = oldVal
            self.readIndex += oldLen
        self.size += 1

    def __str__(self):
        resList = []
        if self.writeIndex > self.readIndex:
            for i in range(self.readIndex, self.writeIndex):
                resList.append(self.tab[i])
        else:
            it = self.readIndex
            while it != self.writeIndex:
                resList.append(self.tab[it])
                it += 1
                if it == len(self.tab):
                    it = 0
        resString = '['
        resString += ', '.join(str(x) for x in resList)
        resString += ']'
        return resString



test = queue()

for i in range(1, 5):
    test.enqueue(i)

print(test.dequeue())

print(test.peek())

print(test)


for i in range(5, 9):
    test.enqueue(i)

print(test.tab)

while(True):
    val = test.dequeue()
    if val is None:
        break;

print(test)