import unittest
from DynamicArray.DynamicArray import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_init_validCapacity_success(self):
        capacity_cases = [(None, 16), (13, 13)]

        for capacity_input, expected_capacity in capacity_cases:
            with self.subTest(capacity_input=capacity_input, expected_capacity=expected_capacity):
                arr = DynamicArray(capacity_input)
                actual_capacity = arr.capacity
                self.assertTrue(actual_capacity, expected_capacity)

    def test_init_wrongCapacity_exception(self):
        capacity_cases = [("1", ValueError), (-1, ValueError)]

        for capacity_input, expected_error in capacity_cases:
            with self.subTest(capacity_input=capacity_input, expected_capacity=expected_error):
                self.assertRaises(expected_error, DynamicArray, capacity_input)

    def test_add(self):
        list_cases = [([1, 1, 'b'], 0, 3, 4, 3, 6),
                      ([1, 1], 0, 2, 3, 3, 6),
                      (['q', 'w'], 'new', 2, 3, 16, 16),
                      ([], 1, 0, 1, 0, 1)]

        for cur_list, new_elem, cur_len, new_len, cur_capa, new_capa in list_cases:
            with self.subTest(cur_list=cur_list, new_elem=new_elem, cur_len=cur_len,
                              new_len=new_elem, cur_capa=cur_capa, new_capa=new_capa):
                dyn_arr = DynamicArray(cur_capa)
                dyn_arr.arr, dyn_arr.len, dyn_arr.capacity = cur_list, cur_len, cur_capa
                dyn_arr.add(new_elem)
                actual_capa = dyn_arr.capacity
                actual_len = dyn_arr.size()
                actual_added_elem = dyn_arr.get(actual_len-1)
                self.assertEqual(actual_capa, new_capa)
                self.assertEqual(actual_len, new_len)
                self.assertEqual(actual_added_elem, new_elem)

    def test_get_validIndex_success(self):
        get_cases = [([1, 2], 2, 0, 1),
                     (['a', 'e', 4], 3, 1, 'e')]

        for list, len, index, expected_get_value in get_cases:
            with self.subTest(list=list, len=len,  index=index, expected_get_value=expected_get_value):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                actual_get_value = dyn_arr.get(index)
                self.assertEqual(actual_get_value, expected_get_value)

    def test_get_wrongIndex_exception(self):
        get_cases = [([1, 2], 2, 5, IndexError),
                     (['a', 'e', 4], 3, -1, IndexError)]

        for list, len, index, expected_get_value in get_cases:
            with self.subTest(list=list, len=len, index=index, expected_get_value=expected_get_value):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                self.assertRaises(IndexError, dyn_arr.get, index)

    def test_set_validIndex_success(self):
        cases = [([1, 2], 2, 0, 5),
                     (['a', 'e', 4], 3, 1, 'f')]

        for list, len, index, expected_set_value in cases:
            with self.subTest(list=list, len=len,  index=index, expected_get_value=expected_set_value):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                dyn_arr.set(index, expected_set_value)
                actual_get_value = dyn_arr.arr[index]
                self.assertEqual(actual_get_value, expected_set_value)

    def test_set_wrongIndex_exception(self):
        cases = [([1, 2], 2, 5, IndexError),
                 (['a', 'e', 4], 3, -1, IndexError)]

        for list, len, index, expected_error in cases:
            with self.subTest(list=list, len=len, index=index, expected_error=expected_error):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                self.assertRaises(expected_error, dyn_arr.set, index, expected_error)

    def test_indexOf(self):
        cases = [([1, 2, 4], 3, 4, 2),
                 (['a', 'e', 4], 3, 5, -1)]

        for list, len, wanted_elem, expected_index in cases:
            with self.subTest(list=list, len=len, wanted_elem=wanted_elem, expected_index=expected_index):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                actual_index = dyn_arr.index_of(wanted_elem)
                self.assertEqual(actual_index, expected_index)

    def test_remove(self):
        cases = [([1, 2, 4], 3, 4, True),
                 (['a', 'e', 4], 3, 5, False)]

        for list, len, wanted_elem, expected_bool in cases:
            with self.subTest(list=list, len=len, wanted_elem=wanted_elem, expected=expected_bool):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                actual_bool = dyn_arr.remove(wanted_elem)
                self.assertEqual(actual_bool, expected_bool)

    def test_removeAt_validIndex_success(self):
        cases = [([1, 2, 4], 3, 0, 1),
                 (['a', 'e', 4], 3, 1, 'e')]

        for list, len, wanted_index, expected_elem in cases:
            with self.subTest(list=list, len=len, wanted_elem=wanted_index, expected=expected_elem):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                actual_elem = dyn_arr.remove_at(wanted_index)
                self.assertEqual(actual_elem, expected_elem)

    def test_removeAt_wrongIndex_failure(self):
        cases = [([1, 2, 4], 3, 4, IndexError),
                 (['a', 'e', 4], 3, -4, IndexError)]

        for list, len, wanted_index, expected_error in cases:
            with self.subTest(list=list, len=len, wanted_elem=wanted_index, expected=expected_error):
                dyn_arr = DynamicArray()
                dyn_arr.arr, dyn_arr.len = list, len
                self.assertRaises(expected_error, dyn_arr.remove_at,wanted_index)