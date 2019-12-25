class DynamicArray:
    def __init__(self, capacity=None):
        self.len = 0
        if capacity is None:
            self.capacity = 16
            self.arr = [None] * self.capacity
        elif not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity should be an integer greater than 0. Was {}.".format(capacity))
        else:
            self.capacity = capacity
            self.arr = [None] * capacity

    def size(self):
        return self.len

    def is_empty(self):
        return self.size() == 0

    def get(self, index):
        if index >= self.len or index < 0:
            raise IndexError("Index should be smaller than {} and greater than 0. Was : {}".format(self.len, index))
        return self.arr[index]

    def set(self, index, elem):
        if index >= self.len or index < 0:
            raise IndexError("Index should be smaller than {} and greater than 0. Was : {}".format(self.len, index))
        self.arr[index] = elem

    def clear(self):
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0

    def add(self, elem):
        if self.len+1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity = 2*self.capacity
        new_arr = [None]*self.capacity
        for i in range(self.len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.arr[self.len] = elem
        self.len += 1

    def remove_at(self, index):
        if index >= self.len or index < 0:
            raise IndexError("Index should be smaller than {} and greater than 0. Was : {}".format(self.len, index))
        data = self.arr[index]
        self.arr = self.arr[0:index] + self.arr[index+1:self.len]
        self.len -= 1
        self.capacity = self.len
        return data

    def index_of(self, elem):
        for i in range(self.len):
            if elem is None:
                if self.arr[i] is None:
                    return i
            elif self.arr[i] == elem:
                return i
        return -1

    def remove(self, elem):
        index = self.index_of(elem)
        if index == -1:
            return False
        else:
            self.remove_at(index)
            return True

    def contains(self, elem):
        return self.index_of(elem) != -1

    def __str__(self):
        return "Array length: {}, Array capacity: {}, Array elements: {}".format(self.len,
                                                                                 self.capacity,
                                                                                 self.arr[0: self.len])
