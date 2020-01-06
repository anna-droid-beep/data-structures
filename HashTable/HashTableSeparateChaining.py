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

