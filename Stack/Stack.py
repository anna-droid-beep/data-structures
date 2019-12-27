class Stack:

    def __init__(self, first_elem=None):
        self.list = list()
        if first_elem is not None:
            self.push(first_elem)

    def get_size(self):
        return len(self.list)

    def push(self, elem):
        self.list.append(elem)

    def pop(self):
        if self.is_empty():
            raise LookupError("Empty stack")
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            raise LookupError("Empty stack")
        return self.list[self.get_size()-1]

    def is_empty(self):
        return self.get_size() == 0

    def __str__(self):
        return str(self.list)
