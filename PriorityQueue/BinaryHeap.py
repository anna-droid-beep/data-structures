from math import floor


class BinaryHeap:
    def __init__(self, size=0, capacity=0, array=None):
        # number of elements currently inside the heap
        self.size = size
        # internal capacity of the heap
        self.capacity = capacity

        self.array = []

        if array is not None:
            self.array = array

        self._position = {}

    @classmethod
    def with_initialized_capacity(cls, size):
        cls.capacity = size
        cls.array = [None] * cls.capacity
        return cls(array=cls.array, capacity=cls.capacity)

    @classmethod
    def with_array(cls, elems):
        h = BinaryHeap.with_initialized_capacity(len(elems))
        for e in elems:
            h.add(e)
        return cls(array=h.array, size=h.size, capacity=h.capacity)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        for i in range(self.capacity):
            self.array[i] = None
        self.size = 0
        self._position.clear()

    def poll(self):
        if self.is_empty():
            return None
        return self.__remove_at(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.array[0]

    def contains(self, elem):
        if elem is None:
            raise TypeError("NoneType is not a valid argument.")
        return elem in self._position.keys()

    def add(self, elem):
        if elem is None:
            raise TypeError("Element shouldn't be of type None")

        if self.size < self.capacity:
            self.array[self.size] = elem
        else:
            self.array.append(elem)
            self.capacity += 1

        self._map_set_position(elem, self.size)
        self.__swim(self.size)
        self.size += 1
        return

    def remove(self, elem):
        if elem is None:
            return False

        index = self._map_get(elem)
        if index is not None:
            self.__remove_at(index)

        return index is not None

    def is_min_heap(self, parent):
        if parent >= self.size:
            return True

        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if left_child < self.size and self.__less(left_child, parent):
            return False
        if right_child < self.size and self.__less(right_child, parent):
            return False

        return self.is_min_heap(left_child) and self.is_min_heap(right_child)

    def __swim(self, k):
        parent = floor((k-1)/2)

        while k > 0 and self.__less(k, parent):
            self.__swap(parent, k)
            k = parent
            parent = floor((k-1)/2)

    def __sink(self, k):
        while True:
            left = 2*k+1
            right = 2*k+2
            smallest = left

            if right < self.size and self.__less(right, left):
                smallest = right

            if left >= self.size or self.__less(k, smallest):
                break

            self.__swap(k, smallest)
            k = smallest

    def __less(self, i, j):
        a = self.array[i]
        b = self.array[j]
        return a < b

    def __swap(self, i, j):
        i_elem = self.array[i]
        j_elem = self.array[j]
        self.array[i] = j_elem
        self.array[j] = i_elem

        self._map_swap(i_elem, j_elem, i, j)

    def __remove_at(self, i):
        if self.is_empty():
            return None

        self.size -= 1
        removed_data = self.array[i]
        self.__swap(i, self.size)
        self.array[self.size] = None
        self._map_remove(removed_data, self.size)

        if i == self.size:
            return removed_data

        elem = self.array[i]
        self.__sink(i)

        if self.array[i] == elem:
            self.__swim(i)

        return removed_data

    def _map_set_position(self, elem, index):
        if elem in self._position.keys():
            self._position[elem].add(index)
        else:
            self._position[elem] = {index}

    def _map_remove(self, elem, index):
        self._position[elem].remove(index)
        if len(self._position[elem]) == 0:
            del self._position[elem]

    def _map_get(self, elem):
        if elem in self._position.keys():
            indices = self._position[elem]
            for index in indices:
                return index
        return None

    def _map_swap(self, e_1, e_2, e_index_1, e_index_2):
        indices_1 = self._position[e_1]
        indices_2 = self._position[e_2]

        indices_1.discard(e_index_1)
        indices_2.discard(e_index_2)

        indices_1.add(e_index_2)
        indices_2.add(e_index_1)


    def __str__(self):
        return str(self.array)