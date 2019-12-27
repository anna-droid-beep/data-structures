class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        print(self.data)


class LinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def clear(self):
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.next = None
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
            self.head = self.tail = Node(elem, next=None)
        else:
            self.tail.next = Node(elem, next=None)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, next=None)
        else:
            new_head = Node(elem, next=self.head)
            self.head = new_head
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
        return data

    def remove_last(self):
        if self.is_empty():
            raise LookupError("Empty list")
        data = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            prev = self.__get_before(self.tail)
            self.tail = prev
            self.tail.next = None
        self.size -= 1
        return data

    def __get_before(self, node):
        trav = self.head
        while trav.next is not node:
            trav = trav.next
        return trav

    def __remove(self, node):
        if node.next is None:
            return self.remove_last()
        previous = self.__get_before(node)
        previous.next = node.next
        data = node.data
        node.data = None
        node.next = None
        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index should be an integer greater than 0 and smaller than {}. Was {}".format(self.size,
                                                                                                            index))
        trav = self.head
        for i in range(index):
            trav = trav.next

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