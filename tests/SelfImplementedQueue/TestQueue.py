from SelfImplementedQueue.Queue import Queue
import unittest

class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_queue = Queue()
        self.filled_queue = Queue("smth")

    def test_getSize(self):
        queue_cases = [ (self.empty_queue, 0), (self.filled_queue, 1)]

        for queue, exp_size in queue_cases:
            with self.subTest(queue=str(queue), exp_size=exp_size):
                act_size = queue.get_size()
                self.assertEqual(act_size, exp_size)

    def test_isEmpty(self):
        queue_cases = [(self.empty_queue, True), (self.filled_queue, False)]

        for queue, exp_emptiness in queue_cases:
            with self.subTest(queue=str(queue), exp_emptiness=exp_emptiness):
                act_emptiness = queue.is_empty()
                self.assertEqual(act_emptiness, exp_emptiness)

    def test_peek_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.empty_queue.peek)

    def test_peek_notEmpty_success(self):
        elem = self.filled_queue.peek()
        self.assertEqual(elem, "smth")
        self.assertEqual(self.filled_queue.get_size(), 1)

    def test_dequeue_isEmpty_raisesError(self):
        self.assertRaises(LookupError, self.empty_queue.dequeue)

    def test_dequeue_notEmpty_raisesError(self):
        elem = self.filled_queue.dequeue()
        self.assertEqual(elem, "smth")
        self.assertEqual(self.filled_queue.get_size(), 0)

    def test_enqueue(self):
        self.filled_queue.enqueue(5)
        self.assertEqual(self.filled_queue.peek(), "smth")
        self.assertEqual(self.filled_queue.get_size(), 2)

    def test_integration(self):
        self.assertEqual(self.empty_queue.get_size(), 0)
        self.assertRaises(LookupError, self.empty_queue.peek)
        self.assertRaises(LookupError, self.empty_queue.dequeue)

        self.empty_queue.enqueue(1)
        self.assertEqual(self.empty_queue.get_size(), 1)
        self.assertEqual(self.empty_queue.peek(), 1)

        self.empty_queue.enqueue(2)
        self.assertEqual(self.empty_queue.get_size(), 2)
        self.assertEqual(self.empty_queue.peek(), 1)

        self.empty_queue.enqueue(3)
        self.assertEqual(self.empty_queue.get_size(), 3)
        self.assertEqual(self.empty_queue.peek(), 1)

        self.assertEqual(self.empty_queue.dequeue(), 1)
        self.assertEqual(self.empty_queue.peek(), 2)
        self.assertEqual(self.empty_queue.get_size(), 2)

        self.assertEqual(self.empty_queue.dequeue(), 2)
        self.assertEqual(self.empty_queue.peek(), 3)
        self.assertEqual(self.empty_queue.get_size(), 1)

        self.assertEqual(self.empty_queue.dequeue(), 3)
        self.assertEqual(self.empty_queue.get_size(), 0)
        self.assertTrue(self.empty_queue.is_empty())
        self.assertRaises(LookupError, self.empty_queue.peek)
        self.assertRaises(LookupError, self.empty_queue.dequeue)