import math

class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = key.hash()

    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        else:
            return self.key == other.key

    def __str__(self):
        return '{{ key: {}, value: {} }}'.format(self.key, self.value)


class HashTableSeparateChaining:

    # default nb of slots in the array
    DEFAULT_CAPACITY = 3

    # default max load factor for a slot
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity=None, maxLoadFactor=None):

        capacity = HashTableSeparateChaining.DEFAULT_CAPACITY if capacity is None else capacity
        if capacity < 0:
            raise ValueError("Capacity should be greater or equal than 0. Was {}".format(capacity))

        maxLoadFactor = HashTableSeparateChaining.DEFAULT_LOAD_FACTOR if maxLoadFactor is None else maxLoadFactor
        if 0 <= maxLoadFactor < 1 is False:
            raise ValueError("Max Load Factor should a float, greater than 0 and smaller than 1. Was {}".format(maxLoadFactor))

        self.capacity = max(HashTableSeparateChaining.DEFAULT_CAPACITY, capacity)
        self.max_load_factor = maxLoadFactor
        self.size = 0
        self.threshold = self.capacity * self.max_load_factor
        self.table = [list() for _ in range(self.capacity)]

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def normalize_index(self, key_hash):
        return (key_hash & 0x7FFFFFFF) % self.capacity

    def clear(self):
        self.table = [list() for _ in range(self.capacity)]
        self.size = 0
