import unittest
from LinkedList.DoublyLinkedList import DoublyLinkedList, Node


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.init_list = DoublyLinkedList()

        self.single_node_list = DoublyLinkedList()
        single_node = Node(data="single", previous=None, next=None)
        self.single_node_list.head = single_node
        self.single_node_list.tail = single_node
        self.single_node_list.size = 1

        self.head_tail_list = DoublyLinkedList()
        head_tail_node1 = Node(data=4, previous=None, next=None)
        head_tail_node2 = Node(data=5, previous=None, next=None)
        head_tail_node1.next = head_tail_node2
        head_tail_node2.previous = head_tail_node1
        self.head_tail_list.head = head_tail_node1
        self.head_tail_list.tail = head_tail_node2
        self.head_tail_list.size = 2

        self.standard_list = DoublyLinkedList()
        standard_head = Node(data=6, previous=None, next=None)
        standard_middle = Node(data=None, previous=None, next=None)
        standard_tail = Node(data=1, previous=None, next=None)
        standard_head.next = standard_tail.previous = standard_middle
        standard_middle.previous = standard_head
        standard_middle.next = standard_tail
        self.standard_list.head = standard_head
        self.standard_list.tail = standard_tail
        self.standard_list.size = 3

    def test_init(self):
        self.assertIsNone(self.init_list.tail)
        self.assertIsNone(self.init_list.head)
        self.assertEqual(self.init_list.size, 0)

    def test_clear(self):
        list_cases = [self.init_list, self.single_node_list, self.head_tail_list, self.standard_list]

        for list in list_cases:
            with self.subTest(list=str(list)):
                list.clear()
                self.assertIsNone(list.tail)
                self.assertIsNone(list.head)
                self.assertEqual(list.size, 0)

    def test_get_size(self):
        list_cases = [(self.init_list, 0), (self.single_node_list, 1),
                      (self.head_tail_list, 2), (self.standard_list, 3)]

        for list, expected_size in list_cases:
            with self.subTest(list=str(list), expected_size=expected_size):
                actual_size = list.get_size()
                self.assertEqual(actual_size, expected_size)

    def test_is_empty(self):
        list_cases = [(self.init_list, True), (self.single_node_list, False),
                      (self.head_tail_list, False), (self.standard_list, False)]

        for list, expected_emptiness in list_cases:
            with self.subTest(list=str(list), expected_emptiness=expected_emptiness):
                actual_emptiness = list.is_empty()
                self.assertEqual(actual_emptiness, expected_emptiness)

    def test_add_isEmpty(self):
        self.init_list.add("new elem")
        self.assertEqual(self.init_list.head.data, "new elem")
        self.assertEqual(self.init_list.tail.data, "new elem")
        self.assertIsNone(self.init_list.head.previous)
        self.assertIsNone(self.init_list.head.next)
        self.assertIsNone(self.init_list.tail.previous)
        self.assertIsNone(self.init_list.tail.next)

    def test_add_notEmpty(self):
        list_cases = [(self.single_node_list, "new", 2), (self.standard_list, 0, 4), (self.head_tail_list, "bla", 3)]

        for list, expected_added, expected_size in list_cases:
            with self.subTest(list=str(list), expected_added=expected_added, expected_size=expected_size):
                list.add(expected_added)
                self.assertEqual(list.tail.data, expected_added)
                self.assertEqual(list.size, expected_size)

    def test_addFirst_isEmpty(self):
        self.init_list.add_first("new elem")
        self.assertEqual(self.init_list.head.data, "new elem")
        self.assertEqual(self.init_list.tail.data, "new elem")
        self.assertIsNone(self.init_list.head.previous)
        self.assertIsNone(self.init_list.head.next)
        self.assertIsNone(self.init_list.tail.previous)
        self.assertIsNone(self.init_list.tail.next)

    def test_addFirst_notEmpty(self):
        list_cases = [(self.single_node_list, "new", 2), (self.standard_list, 0, 4), (self.head_tail_list, "bla", 3)]

        for list, expected_added, expected_size in list_cases:
            with self.subTest(list=str(list), expected_added=expected_added, expected_size=expected_size):
                list.add_first(expected_added)
                self.assertEqual(list.head.data, expected_added)
                self.assertEqual(list.size, expected_size)

    def test_peekFirst_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.init_list.peek_first)

    def test_peekFirst_notEmpty_success(self):
        list_cases = [(self.single_node_list, "single"),
                      (self.head_tail_list, 4),
                      (self.standard_list, 6)]

        for list, expected_head in list_cases:
            with self.subTest(list=str(list), expected_head=expected_head):
                actual_head = list.peek_first()
                self.assertEqual(actual_head, expected_head)

    def test_peekLast_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.init_list.peek_last)

    def test_peekLast_notEmpty_success(self):
        list_cases = [(self.single_node_list, "single"),
                      (self.head_tail_list, 5),
                      (self.standard_list, 1)]

        for list, expected_head in list_cases:
            with self.subTest(list=str(list), expected_head=expected_head):
                actual_head = list.peek_last()
                self.assertEqual(actual_head, expected_head)

    def test_removeFirst_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.init_list.remove_first)

    def test_removeFirst_notEmpty_success(self):
        list_cases = [(self.single_node_list, "single", 0),
                      (self.head_tail_list, 4, 1),
                      (self.standard_list, 6, 2)]

        for list, expected_head, expected_size in list_cases:
            with self.subTest(list=str(list), expected_head=expected_head, expected_size=expected_size):
                actual_head = list.remove_first()
                self.assertEqual(actual_head, expected_head)
                self.assertEqual(list.size, expected_size)

    def test_removeLast_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.init_list.remove_last)

    def test_removeLast_notEmpty_success(self):
        list_cases = [(self.single_node_list, "single", 0),
                      (self.head_tail_list, 5, 1),
                      (self.standard_list, 1, 2)]

        for list, expected_tail, expected_size in list_cases:
            with self.subTest(list=str(list), expected_head=expected_tail, expected_size=expected_size):
                actual_tail = list.remove_last()
                self.assertEqual(actual_tail, expected_tail)
                self.assertEqual(list.size, expected_size)

    def test_removeAt_wrongIndex_raisesError(self):
        list_cases = [ (self.init_list, 5), (self.single_node_list, -1),
                       (self.head_tail_list, 4), (self.standard_list, 4)]

        for list, lookup_index in list_cases:
            with self.subTest(list=str(list), lookup_index=lookup_index):
                self.assertRaises(IndexError, list.remove_at, lookup_index)

    def test_removeAt_validIndex_success(self):
        list_cases = [(self.single_node_list, 0, "single"),
                       (self.head_tail_list, 1, 5), (self.standard_list, 1, None)]

        for list, lookup_index, expected_data in list_cases:
            with self.subTest(list=str(list), lookup_index=lookup_index, expected_data=expected_data):
                actual_data = list.remove_at(lookup_index)
                self.assertEqual(actual_data, expected_data)

    def test_remove(self):
        list_cases = [(self.init_list, "s", False), (self.single_node_list, "single", True),
                       (self.head_tail_list, None, False), (self.standard_list, None, True)]

        for list, lookup_value, expected_removing in list_cases:
            with self.subTest(list=str(list), lookup_value=lookup_value, expected_removing=expected_removing):
                actual_removing = list.remove(lookup_value)
                self.assertEqual(actual_removing, expected_removing)

    def test_indexOf(self):
        list_cases = [(self.init_list, "s", -1), (self.single_node_list, "single", 0),
                       (self.head_tail_list, 5, 1), (self.standard_list, None, 1)]

        for list, lookup_value, expected_index in list_cases:
            with self.subTest(list=str(list), lookup_value=lookup_value, expected_removing=expected_index):
                actual_index = list.index_of(lookup_value)
                self.assertEqual(actual_index, expected_index)

    def test_contains(self):
        list_cases = [(self.init_list, None, False), (self.single_node_list, "double", False),
                      (self.head_tail_list, 4, True), (self.standard_list, 10, False)]

        for list, lookup_value, expected_contain in list_cases:
            with self.subTest(list=str(list), lookup_value=lookup_value, expected_contain=expected_contain):
                actual_contain = list.contains(lookup_value)
                self.assertEqual(actual_contain, expected_contain)

    def test_integration(self):
        l = DoublyLinkedList()
        self.assertTrue(l.is_empty())

        l.add(5)
        self.assertTrue(l.contains(5))
        self.assertEqual(l.peek_first(), 5)
        self.assertEqual(l.peek_last(), 5)

        l.add(4)
        self.assertEqual(l.peek_first(), 5)
        self.assertEqual(l.peek_last(), 4)

        l.add(10)
        self.assertEqual(l.peek_first(), 5)
        self.assertEqual(l.peek_last(), 10)

        l.add(8)
        l.add(4)

        l.add_first(1)
        self.assertEqual(l.peek_first(), 1)
        self.assertEqual(l.peek_last(), 4)

        # linked_list 1 5 4 10 8 4

        removed_1 = l.remove(4)
        self.assertTrue(removed_1)

        removed_2 = l.remove(4)
        self.assertTrue(removed_2)

        unremoved = l.remove(4)
        self.assertFalse(unremoved)

        first = l.remove_first()
        self.assertEqual(first, 1)

        last = l.remove_last()
        self.assertEqual(last, 8)

        # linked_list 5 10

        removed_3 = l.remove_at(1)
        removed_4 = l.remove_at(0)

        self.assertEqual(removed_3, 10)
        self.assertEqual(removed_4, 5)

        self.assertRaises(LookupError, l.peek_first)
        self.assertRaises(LookupError, l.peek_last)
        self.assertRaises(IndexError, l.remove_at, 0)
        self.assertRaises(LookupError, l.remove_last)
        self.assertRaises(LookupError, l.remove_first)
