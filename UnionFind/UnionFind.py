class UnionFind:
    def __init__(self, size=0, sz=None, parent=None):
        # number of elements in the union find
        self.size = size

        # number of components in the union find
        self.nb_components = size

        # size of each sets
        self.sz = []
        if sz is not None:
            self.sz = sz

        # parent of node i. i is root if id[i] = i
        self.parents = []
        if parent is not None:
            self.parents = parent

    @classmethod
    def with_size(cls, size):
        if size <= 0:
            raise ValueError("Size should be greater than 0. Was {}".format(size))
        sz = [1]*size
        parent = [i for i in range(size)]
        return cls(size=size, sz=sz, parent=parent)

    def find(self, p):
        root = p

        while self.parents[root] != root:
            root = self.parents[root]

        while p != root:
            tmp = self.parents[p]
            self.parents[p] = root
            p = tmp

        return root

    def are_connected(self, p, q):
        return self.find(p) == self.find(q)

    def component_size(self, p):
        return self.sz[self.find(p)]

    def get_size(self):
        return self.size

    def get_components(self):
        return self.nb_components

    def unify(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        if self.sz[root_p] < self.sz[root_q]:
            self.sz[root_q] += self.sz[root_p]
            self.parents[root_p] = self.parents[root_q]
        else:
            self.sz[root_p] += self.sz[root_q]
            self.parents[root_q] = self.parents[root_p]

        self.nb_components -= 1
