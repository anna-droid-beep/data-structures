from LinkedList.DoublyLinkedList import DoublyLinkedList


class Queue:

    def __init__(self, first_elem=None):
        self.list = DoublyLinkedList()
        if first_elem is not None:
            self.enqueue(first_elem)

    def get_size(self):
        return self.list.get_size()

    def is_empty(self):
        return self.get_size() == 0

    def peek(self):
        if self.is_empty():
            raise LookupError("Empty Queue")
        return self.list.peek_first()

    def dequeue(self):
        if self.is_empty():
            raise LookupError("Empty Queue")
        return self.list.remove_first()

    def enqueue(self, elem):
        self.list.add(elem)

    def __str__(self):
        return str(self.list)