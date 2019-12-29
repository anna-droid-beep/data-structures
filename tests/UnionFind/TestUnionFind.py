import unittest
from UnionFind.UnionFind import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_uf = UnionFind()
        self.filled_uf = UnionFind.with_size(9)

        self.set_1 = [1, 1, 1, 2, 3, 6, 6, 6, 8]

    def test_withSize_wrongSize_raisesError(self):
        cases = [-1, 0]

        for case in cases:
            with self.subTest(size = case):
                self.assertRaises(ValueError, UnionFind.with_size, case)

    def test_withSize_validSize(self):
        cases = [(2, 2, [0, 1], [1, 1]), (4, 4, [0, 1, 2, 3], [1, 1, 1, 1])]

        for size, exp_nb_components, exp_parents, exp_sz in cases:
            with self.subTest(size=size, exp_nb_components=exp_nb_components, exp_parents=exp_parents, exp_sz=exp_sz):
                uf = UnionFind.with_size(size)
                act_size = uf.size
                act_nb_components = uf.nb_components
                act_parent = uf.parents
                act_sz = uf.sz
                self.assertEqual(act_size, size)
                self.assertEqual(act_nb_components, exp_nb_components)
                self.assertListEqual(act_parent, exp_parents)
                self.assertListEqual(act_sz, exp_sz)

    def test_find(self):
        cases = [(0, 1, [1, 1, 1, 2, 3, 6, 6, 6, 8]), (1, 1, [1, 1, 1, 2, 3, 6, 6, 6, 8]),
                 (2, 1, [1, 1, 1, 2, 3, 6, 6, 6, 8]), (3, 1, [1, 1, 1, 1, 3, 6, 6, 6, 8]),
                 (4, 1, [1, 1, 1, 1, 1, 6, 6, 6, 8])]

        for elem, exp_parent, exp_parents in cases:
            with self.subTest(elem=elem, exp_parent=exp_parent, exp_parents=exp_parents):
                self.filled_uf.parents = self.set_1
                act_parent = self.filled_uf.find(elem)
                act_parents = self.filled_uf.parents
                self.assertEqual(act_parent, exp_parent)
                self.assertListEqual(act_parents, exp_parents)

    def test_areConnected(self):
        cases = [(0, 2, True), (1, 4, True), (5, 4, False), (2, 7, False), (8, 5, False)]

        for p, q, exp_connectivity in cases:
            with self.subTest(p=p, q=q, exp_connectivity=exp_connectivity):
                self.filled_uf.parents = self.set_1
                act_connectivity = self.filled_uf.are_connected(p, q)
                self.assertEqual(act_connectivity, exp_connectivity)

    def test_component_size(self):
        cases = range(9)

        for elem in cases:
            with self.subTest(case=elem):
                act_size = self.filled_uf.component_size(elem)
                self.assertEqual(act_size, 1)

    def test_unify(self):
        cases = [(0, 1, [2, 1, 1, 1], [0, 0, 2, 3]),
                 (1, 1, [1, 1, 1, 1], [0, 1, 2, 3]),
                 (0, 3, [2, 1, 1, 1], [0, 1, 2, 0])]

        for p, q, exp_sz, exp_parents in cases:
            with self.subTest(p=p, q=q, exp_sz=exp_sz, exp_parents=exp_parents):
                uf = UnionFind.with_size(4)
                uf.unify(p, q)
                act_sz = uf.sz
                act_parents = uf.parents
                self.assertListEqual(act_sz, exp_sz)
                self.assertListEqual(act_parents, exp_parents)

    def test_integration(self):
        uf = UnionFind.with_size(5)
        self.assertEqual(uf.size, 5)
        self.assertEqual(uf.nb_components, 5)
        self.assertListEqual(uf.parents, [0, 1, 2, 3, 4])
        self.assertListEqual(uf.sz, [1, 1, 1, 1, 1])

        uf.unify(0, 1)
        self.assertEqual(uf.size, 5)
        self.assertEqual(uf.nb_components, 4)
        self.assertListEqual(uf.parents, [0, 0, 2, 3, 4])
        self.assertListEqual(uf.sz, [2, 1, 1, 1, 1])

        uf.unify(4, 3)
        self.assertEqual(uf.size, 5)
        self.assertEqual(uf.nb_components, 3)
        self.assertListEqual(uf.parents, [0, 0, 2, 4, 4])
        self.assertListEqual(uf.sz, [2, 1, 1, 1, 2])

        uf.unify(4, 0)
        self.assertEqual(uf.size, 5)
        self.assertEqual(uf.nb_components, 2)
        self.assertListEqual(uf.parents, [4, 0, 2, 4, 4])
        self.assertListEqual(uf.sz, [2, 1, 1, 1, 4])

        act_component_size = uf.component_size(1)
        self.assertEqual(act_component_size, 4)
        self.assertEqual(uf.size, 5)
        self.assertEqual(uf.nb_components, 2)
        self.assertListEqual(uf.parents, [4, 4, 2, 4, 4])
        self.assertListEqual(uf.sz, [2, 1, 1, 1, 4])

        self.assertTrue(uf.are_connected(3, 4))
        self.assertFalse(uf.are_connected(2, 0))