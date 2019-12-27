class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __str__(self):
        print(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def clear(self):
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.previous = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def add(self, elem):
        self.add_last(elem)

    def add_last(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, previous=None, next=None)
        else:
            self.tail.next = Node(elem, previous=self.tail, next=None)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, previous=None, next=None)
        else:
            self.head.previous = Node(elem, previous=None, next=self.head)
            self.head = self.head.previous
        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise LookupError("Empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise LookupError("Empty list")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise LookupError("Empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.previous = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise LookupError("Empty list")
        data = self.tail.data
        self.tail = self.tail.previous
        self.size -=1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def __remove(self, node):
        if node.previous is None:
            return self.remove_first()
        if node.next is None:
            return self.remove_last()
        node.previous.next = node.next
        node.next.previous = node.previous
        data = node.data
        node.data = None
        node.previous = node.next = None
        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index should be an integer greater than 0 and smaller than {}. Was {}".format(self.size,
                                                                                                            index))
        if index < self.size/2:
            trav = self.head
            for i in range(index):
                trav = trav.next
        else:
            trav = self.tail
            for i in range(self.size-1, index, -1):
                trav = trav.previous
        return self.__remove(trav)

    def remove(self, value):
        trav = self.head
        if value is None:
            while trav is not None:
                if trav.data is None:
                    self.remove(trav)
                    return True
                trav = trav.next
        else:
            while trav is not None:
                if trav.data == value:
                    self.__remove(trav)
                    return True
                trav = trav.next
        return False

    def index_of(self, value):
        trav = self.head
        index = 0
        if value is None:
            while trav is not None:
                if trav.data is None:
                    return index
                trav = trav.next
                index += 1
        else:
            while trav is not None:
                if trav.data == value:
                    return index
                trav = trav.next
                index += 1
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    def __str__(self):
        trav = self.head
        printed_data = ""
        while trav is not None:
            printed_data += "{}".format(trav.data)
            if trav.next is not None:
                printed_data += ", "
            trav = trav.next
        return printed_data