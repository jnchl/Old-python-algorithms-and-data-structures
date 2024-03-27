class List:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = DataBlock(data)
        else:
            newHead = DataBlock(data)
            newHead.next = self.head
            self.head = newHead

    def append(self, data):
        if self.head is None:
            self.head = DataBlock(data)
        else:
            ogHead = self.head
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = DataBlock(data)
            self.head = ogHead

    def remove(self):
        if self.head is None:
            print("Nothing to remove")
        else:
            self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            print("Nothing to remove")
        elif self.head.next is None:
            self.head = None
        else:
            ogHead = self.head
            previousHead = self.head
            while self.head.next is not None:
                previousHead = self.head
                self.head = self.head.next
            previousHead.next = None
            self.head = ogHead

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        ogHead = self.head
        leng = 0
        while self.head is not None:
            leng += 1
            self.head = self.head.next
        self.head = ogHead
        return leng

    def get(self):
        return self.head.data

    def print(self):
        ogHead = self.head
        while self.head is not None:
            print("-> {}".format(self.head.data))
            self.head = self.head.next
        self.head = ogHead


class DataBlock:
    def __init__(self, data=None):
        self.data = data
        self.next = None


uniData = [('AGH', 'Kraków', 1919),
           ('UJ', 'Kraków', 1364),
           ('PW', 'Warszawa', 1915),
           ('UW', 'Warszawa', 1915),
           ('UP', 'Poznań', 1919),
           ('PG', 'Gdańsk', 1945)]

uczelnie = List()
uczelnie.append(uniData[0])
uczelnie.append(uniData[1])
uczelnie.append(uniData[2])
uczelnie.add(uniData[3])
uczelnie.add(uniData[4])
uczelnie.add(uniData[5])
uczelnie.print()
print(uczelnie.length())
uczelnie.remove()
print(uczelnie.get())
uczelnie.remove_end()
uczelnie.print()
uczelnie.destroy()
print(uczelnie.is_empty())
uczelnie.remove()
uczelnie.append(uniData[0])
uczelnie.remove_end()
uczelnie.print()