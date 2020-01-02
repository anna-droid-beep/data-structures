import unittest
from BinarySearchTree.BinarySearchTree import BinarySearchTree, Node
from BinarySearchTree.TreeTraversalOrder import TreeTraversalOrder


class MockBST:

    def __init__(self):
        # With Level-Order/BFS printing, the BST is 3, 1, 5, 2, 4, 7, 8
        root_1 = Node(3)
        root_1.left = Node(1, left=None, right=Node(2))
        root_1.right = Node(5, left=Node(4), right=Node(7, left=Node(6), right=Node(8)))
        self.bst_1 = BinarySearchTree(root=root_1, node_count=8)

        # With Level-Order/BFS printing, the BST is 5, 4, 3
        root_2 = Node(5, left=Node(4, left=Node(3)))
        self.bst_2 = BinarySearchTree(root=root_2, node_count=3)

        self.bst_3 = BinarySearchTree()


class TestBinarySearchTree(unittest.TestCase):

    def test_add(self):
        cases = [(9, True, 9), (0, True, 9), (1, False, 8), (2, False, 8)]

        for elem, exp_add, exp_size in cases:
            with self.subTest(elem=elem, exp_add=exp_add, exp_size=exp_size):
                mock_bst = MockBST()
                act_add = mock_bst.bst_1.add(elem)
                actual_size = mock_bst.bst_1.node_count
                self.assertEqual(act_add, exp_add)
                self.assertEqual(actual_size, exp_size)

    def test_remove(self):
        cases = [(3, True, 7), (1, True, 7), (5, True, 7), (9, False, 8)]

        for elem, exp_remove, exp_size in cases:
            with self.subTest(elem=elem, exp_remove=exp_remove, exp_size=exp_size):
                mock_bst = MockBST()
                act_remove = mock_bst.bst_1.remove(elem)
                actual_size = mock_bst.bst_1.node_count
                self.assertEqual(act_remove, exp_remove)
                self.assertEqual(actual_size, exp_size)

    def test_contains(self):
        cases = [(0, False), (1, True), (2, True), (3, True),
                 (9, False), (10, False)]
        bst = MockBST().bst_1

        for elem, exp_exists in cases:
            with self.subTest(elem=elem, exp_exists=exp_exists):
                act_exists = bst.contains(elem)
                self.assertEqual(act_exists, exp_exists)

    def test_isEmpty(self):
        mock_bst = MockBST()
        cases = [(mock_bst.bst_1, False), (mock_bst.bst_2, False), (mock_bst.bst_3, True)]

        for bst, exp_emptiness in cases:
            with self.subTest(bst=str(bst), exp_emptiness=exp_emptiness):
                act_emptiness = bst.is_empty()
                self.assertEqual(act_emptiness, exp_emptiness)

    def test_getSize(self):
        mock_bst = MockBST()
        cases = [(mock_bst.bst_1, 8), (mock_bst.bst_2, 3), (mock_bst.bst_3, 0)]

        for bst, exp_size in cases:
            with self.subTest(bst=str(bst), exp_size=exp_size):
                act_size = bst.get_size()
                self.assertEqual(act_size, exp_size)

    def test_traverse(self):
        mock_bst = MockBST()

        cases = [(mock_bst.bst_1, TreeTraversalOrder.LEVEL_ORDER, "{ 3 1 5 2 4 7 6 8 }"),
                 (mock_bst.bst_1, TreeTraversalOrder.PRE_ORDER, "{ 3 1 2 5 4 7 6 8 }"),
                 (mock_bst.bst_1, TreeTraversalOrder.IN_ORDER, "{ 1 2 3 4 5 6 7 8 }"),
                 (mock_bst.bst_1, TreeTraversalOrder.POST_ORDER, "{ 2 1 4 6 8 7 5 3 }"),
                 (mock_bst.bst_2, TreeTraversalOrder.LEVEL_ORDER, "{ 5 4 3 }"),
                 (mock_bst.bst_2, TreeTraversalOrder.PRE_ORDER, "{ 5 4 3 }"),
                 (mock_bst.bst_2, TreeTraversalOrder.IN_ORDER, "{ 3 4 5 }"),
                 (mock_bst.bst_2, TreeTraversalOrder.POST_ORDER, "{ 3 4 5 }"),
                 (mock_bst.bst_3, TreeTraversalOrder.LEVEL_ORDER, '{ }'),
                 (mock_bst.bst_3, TreeTraversalOrder.PRE_ORDER, '{ }'),
                 (mock_bst.bst_3, TreeTraversalOrder.IN_ORDER,  '{ }'),
                 (mock_bst.bst_3, TreeTraversalOrder.POST_ORDER, '{ }')]

        for bst, strategy, exp_order in cases:
            with self.subTest(bst=str(bst), strategy=strategy, exp=exp_order):
                act_bfs = bst.traverse(strategy)
                self.assertEqual(act_bfs, exp_order)

    def test_height(self):
        mock_bst = MockBST()
        cases = [(mock_bst.bst_1, 4), (mock_bst.bst_2, 3), (mock_bst.bst_3, 0)]
        for bst, exp_height in cases:
            with self.subTest(bst=str(bst), exp_height=exp_height):
                act_height = bst.height()
                self.assertEqual(act_height, exp_height)

    def test_integration(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

        bst.add("A")
        self.assertTrue(bst.contains("A"))
        self.assertEqual(str(bst), "{ A }")

        bst.add("Z")
        bst.add("D")
        bst.add("E")
        bst.add("K")
        self.assertEqual(bst.get_size(), 5)
        self.assertEqual(str(bst), "{ A Z D E K }")

        bst.remove("A")
        self.assertEqual(bst.get_size(), 4)
        self.assertEqual(str(bst), "{ Z D E K }")

        bst.add("ZOO")
        bst.add("ZEBRA")
        self.assertEqual(bst.get_size(), 6)
        self.assertEqual(str(bst), "{ Z D ZOO E ZEBRA K }")

        bst.remove("Z")
        self.assertEqual(bst.get_size(), 5)
        self.assertEqual(str(bst), "{ ZEBRA D ZOO E K }")
