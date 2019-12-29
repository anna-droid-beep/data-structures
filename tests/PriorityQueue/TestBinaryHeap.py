import unittest
from PriorityQueue.BinaryHeap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_heap = BinaryHeap()

        self.filled_heap = BinaryHeap()
        self.filled_heap.array = [4, 5, 4, 6, 8, 6]
        self.filled_heap._position = {4: {0, 2}, 5: {1}, 6: {3, 5}, 8: {4}}
        self.filled_heap.size = 6
        self.filled_heap.capacity = 6

        self.heap_array_1 = [1, 2, 3, 4, 4, 5, 5, 6]
        self.heap_array_2 = [1]
        self.heap_array_3 = [1, 2]

        self.not_heap_array_1 = [10, 12, 20, 11, 20]
        self.not_heap_array_2 = [10, 12, 20, 20, 11, 5]
        self.not_heap_array_3 = [10, 13, 20, 11]

    def test_withInitializedCapacity(self):
        capa_heap = BinaryHeap.with_initialized_capacity(3)
        self.assertEqual(capa_heap.size, 0)
        self.assertEqual(capa_heap.capacity, 3)
        self.assertEqual(capa_heap.array, [None]*3)

    def test_withArray(self):
        array_heap_cases = [(self.not_heap_array_1, 5, 5, [10, 11, 20, 12, 20]),
                            (self.not_heap_array_2, 6, 6, [5, 11, 10, 20, 12, 20]),
                            (self.not_heap_array_3, 4, 4, [10, 11, 20, 13])]

        for array, exp_size, exp_capa, exp_array in array_heap_cases:
            with self.subTest(array=array, exp_size=exp_size, exp_capa=exp_capa, exp_array=exp_array):
                heap = BinaryHeap.with_array(array)
                act_size = heap.size
                act_capa = heap.capacity
                act_array = heap.array
                self.assertEqual(act_size, exp_size)
                self.assertEqual(act_capa, exp_capa)
                self.assertEqual(act_array, exp_array)

    def test_remove(self):
        elem_cases = [(4, True), (5, True), (6, True), (8, True),
                      (0, False), (6, True), (8, False), (5, False),
                      (4, True), (1, False)]

        for elem, exp_removal in elem_cases:
            with self.subTest(elem=elem, exp_removal=exp_removal):
                act_removal = self.filled_heap.remove(elem)
                self.assertEqual(act_removal, exp_removal)

    def test_add_extendCapacity(self):
        elem_cases = [(1, [1, 5, 4, 6, 8, 6, 4], 7, 7),
                      (2, [1, 2, 4, 5, 8, 6, 4, 6], 8, 8),
                      (10, [1, 2, 4, 5, 8, 6, 4, 6, 10], 9, 9)]

        for elem, exp_arr, exp_capacity, exp_size in elem_cases:
            with self.subTest(elem=elem, exp_arr=exp_arr, exp_capacity=exp_capacity, exp_size=exp_size):
                self.filled_heap.add(elem)
                act_arr = self.filled_heap.array
                act_capacity = self.filled_heap.capacity
                act_size = self.filled_heap.size
                self.assertEqual(act_arr, exp_arr)
                self.assertEqual(act_capacity, exp_capacity)
                self.assertEqual(act_size, exp_size)

    def test_add_notExtendCapacity(self):
        elem_cases = [(1, [1, 5, 4, 6, 8, 6, 4, None, None, None], 10, 7),
                      (2, [1, 2, 4, 5, 8, 6, 4, 6, None, None], 10, 8),
                      (10, [1, 2, 4, 5, 8, 6, 4, 6, 10, None], 10, 9)]

        array_with_none = self.filled_heap.array + [None]*4
        self.filled_heap.array = array_with_none
        self.filled_heap.capacity = 10
        for elem, exp_arr, exp_capacity, exp_size in elem_cases:
            with self.subTest(elem=elem, exp_arr=exp_arr, exp_capacity=exp_capacity, exp_size=exp_size):
                self.filled_heap.add(elem)
                act_arr = self.filled_heap.array
                act_capacity = self.filled_heap.capacity
                act_size = self.filled_heap.size
                self.assertEqual(act_arr, exp_arr)
                self.assertEqual(act_capacity, exp_capacity)
                self.assertEqual(act_size, exp_size)

    def test_add_noneType_raisesError(self):
        self.assertRaises(TypeError, self.filled_heap.add, None)

    def test_isEmpty(self):
        heap_cases = [(self.empty_heap, True), (self.filled_heap, False)]

        for heap, exp_emptiness in heap_cases:
            with self.subTest(heap=heap, exp_emptiness=exp_emptiness):
                act_emptiness = heap.is_empty()
                self.assertEqual(act_emptiness, exp_emptiness)

    def test_clear(self):
        array_cases = [self.heap_array_1, self.heap_array_2, self.heap_array_3]

        for array in array_cases:
            with self.subTest(array=array):
                heap = BinaryHeap.with_array(array)
                heap.clear()
                self.assertEqual(heap.size, 0)
                self.assertEqual(heap.capacity, len(array))
                self.assertListEqual(heap.array, [None]*len(array))

    def test_poll(self):
        heap_cases = [(self.filled_heap, 4, 5), (self.empty_heap, None, 0)]

        for heap, exp_polled, exp_size in heap_cases:
            with self.subTest(heap=str(heap), exp_polled=exp_polled, exp_size=exp_size):
                act_polled = heap.poll()
                act_size = heap.size
                self.assertEqual(act_polled, exp_polled)
                self.assertEqual(act_size, exp_size)

    def test_peek(self):
        heap_cases = [(self.filled_heap, 4, 6), (self.empty_heap, None, 0)]

        for heap, exp_peeked, exp_size in heap_cases:
            with self.subTest(heap=str(heap), exp_peeked=exp_peeked, exp_size=exp_size):
                act_polled = heap.peek()
                act_size = heap.size
                self.assertEqual(act_polled, exp_peeked)
                self.assertEqual(act_size, exp_size)

    def test_contains_validType(self):
        elems_case = [(1, False), (2, False), (3, False), (4, True), (5, True)]

        for elem, exp_contain in elems_case:
            with self.subTest(elem=elem, exp_contain=exp_contain):
                act_contain = self.filled_heap.contains(elem)
                self.assertEqual(act_contain, exp_contain)

    def test_contains_noneType_raisesError(self):
        self.assertRaises(TypeError, self.filled_heap.contains, None)

    def test_mapSwap(self):
        self.filled_heap._map_swap(4, 5, 0, 1)
        self.assertSetEqual(self.filled_heap._position[4], {1, 2})
        self.assertSetEqual(self.filled_heap._position[5], {0})

    def test_mapGet(self):
        map_cases = [(4, 0), (5, 1), (6, 3), (8, 4), (0, None)]

        for elem, exp_index in map_cases:
            with self.subTest(elem=elem, exp_index=exp_index):
                act_index = self.filled_heap._map_get(elem)
                self.assertEqual(exp_index, act_index)

    def test_mapRemove_notEmptySet_success(self):
        map_cases = [(4, 0, {2}), (6, 5, {3})]

        for elem, index, exp_set in map_cases:
            with self.subTest(elem=elem, index=index, exp_set=exp_set):
                self.filled_heap._map_remove(elem, index)
                act_set = self.filled_heap._position[elem]
                self.assertSetEqual(act_set, exp_set)

    def test_mapRemove_emptySet_deleteKey(self):
        map_cases = [(5, 1), (8, 4)]

        for elem, index in map_cases:
            with self.subTest(elem=elem, index=index):
                self.filled_heap._map_remove(elem, index)
                self.assertFalse(elem in self.filled_heap._position.keys())

    def test_mapSetPosition(self):
        map_cases = [(0, 6, {6}), (10, 7, {7}),
                     (5, 8, {1, 8}), (4, 9, {0, 2, 9})]

        for elem, index, exp_set in map_cases:
            with self.subTest(elem=elem, index=index, exp_set=exp_set):
                self.filled_heap._map_set_position(elem, index)
                act_set = self.filled_heap._position[elem]
                self.assertSetEqual(act_set, exp_set)

    def test_isMinHeap(self):

        heap_cases = [(self.heap_array_1, True), (self.heap_array_2, True), (self.heap_array_3, True),
                      (self.not_heap_array_1, False), (self.not_heap_array_2, False), (self.not_heap_array_3, False)]

        for arr, exp_heapiness in heap_cases:
            with self.subTest(arr=arr, exp_heapiness=exp_heapiness):
                dummy_heap = BinaryHeap()
                dummy_heap.array = arr
                dummy_heap.size = len(arr)
                act_heapiness = dummy_heap.is_min_heap(0)
                self.assertEqual(act_heapiness, exp_heapiness)

    def test_integration(self):
        self.empty_heap.add(5)
        self.empty_heap.add(0)
        self.empty_heap.add(4)
        self.empty_heap.add(1)
        self.empty_heap.add(3)
        self.empty_heap.add(2)

        self.assertEqual(self.empty_heap.size, 6)
        self.assertEqual(self.empty_heap.capacity, 6)
        self.assertListEqual(self.empty_heap.array, [0, 1, 2, 5, 3, 4])

        act_pol_1 = self.empty_heap.poll()
        self.assertEqual(act_pol_1, 0)
        self.assertEqual(self.empty_heap.size, 5)
        self.assertEqual(self.empty_heap.capacity, 6)
        self.assertListEqual(self.empty_heap.array, [1, 3, 2, 5, 4, None])

        act_peek_1 = self.empty_heap.peek()
        self.assertEqual(act_peek_1, 1)
        self.assertEqual(self.empty_heap.size, 5)
        self.assertEqual(self.empty_heap.capacity, 6)
        self.assertListEqual(self.empty_heap.array, [1, 3, 2, 5, 4, None])

        act_removal_1 = self.empty_heap.remove(4)
        act_removal_2 = self.empty_heap.remove(0)
        self.assertTrue(act_removal_1)
        self.assertFalse(act_removal_2)
        self.assertEqual(self.empty_heap.size, 4)
        self.assertEqual(self.empty_heap.capacity, 6)
        self.assertListEqual(self.empty_heap.array, [1, 3, 2, 5, None, None])
