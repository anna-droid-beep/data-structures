import unittest
from Stack.Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.init_empty_stack = Stack()
        self.init_filled_stack = Stack("smth")

    def test_isEmpty(self):
        stack_cases = [ (self.init_empty_stack, True),
                        (self.init_filled_stack, False)]

        for stack, expected_emptiness in stack_cases:
            with self.subTest(stack=str(stack), emptiness=expected_emptiness):
                actual_emptiness = stack.is_empty()
                self.assertEqual(actual_emptiness, expected_emptiness)

    def test_getSize(self):
        stack_cases = [(self.init_empty_stack, 0),
                       (self.init_filled_stack, 1)]

        for stack, expected_size in stack_cases:
            with self.subTest(stack=str(stack), size=expected_size):
                actual_size = stack.get_size()
                self.assertEqual(actual_size, expected_size)

    def test_push(self):
        stack_cases = [(self.init_empty_stack, "1"),
                       (self.init_filled_stack, "else")]

        for stack, exp_added_elem in stack_cases:
            with self.subTest(stack=str(stack), size=exp_added_elem):
                stack.push(exp_added_elem)
                self.assertEqual(stack.peek(), exp_added_elem)

    def test_pop_emptyStack_raisesError(self):
        self.assertRaises(LookupError, self.init_empty_stack.pop)

    def test_pop_filledStack_success(self):
        popped = self.init_filled_stack.pop()
        self.assertEqual(popped, "smth")
        self.assertEqual(self.init_filled_stack.get_size(), 0)

    def test_peek_emptyStack_raisesError(self):
        self.assertRaises(LookupError, self.init_empty_stack.peek)

    def test_peek_filledStack_success(self):
        peeked = self.init_filled_stack.peek()
        self.assertEqual(peeked, "smth")
        self.assertEqual(self.init_filled_stack.get_size(), 1)

    def test_integration(self):
        self.assertEqual(self.init_filled_stack.get_size(), 1)
        self.assertFalse(self.init_filled_stack.is_empty())
        self.assertEqual(self.init_filled_stack.peek(), "smth")

        self.init_filled_stack.push("else")

        self.assertEqual(self.init_filled_stack.get_size(), 2)
        self.assertFalse(self.init_filled_stack.is_empty())
        self.assertEqual(self.init_filled_stack.peek(), "else")

        pop_1 = self.init_filled_stack.pop()

        self.assertEqual(self.init_filled_stack.get_size(), 1)
        self.assertFalse(self.init_filled_stack.is_empty())
        self.assertEqual(pop_1, "else")
        self.assertEqual(self.init_filled_stack.peek(), "smth")

        pop_2 = self.init_filled_stack.pop()

        self.assertEqual(self.init_filled_stack.get_size(), 0)
        self.assertTrue(self.init_filled_stack.is_empty())
        self.assertEqual(pop_2, "smth")
        self.assertRaises(LookupError, self.init_filled_stack.pop)
        self.assertRaises(LookupError, self.init_filled_stack.peek)
