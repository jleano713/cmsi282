import unittest
import random
from priorityqueue import PriorityQueue

class PriorityQueueTestCase(unittest.TestCase):

    def test_new_priority_queues_are_empty(self):
        q = PriorityQueue()
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), '[]')

    def test_remove_from_new_priority_queue_raises(self):
        q = PriorityQueue()
        self.assertRaises(q.remove)

    def test_peek_works_on_one_element_queue(self):
        q = PriorityQueue()
        q.add(7)
        self.assertEqual(q.peek(), 7)
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), '[7]')

    def test_add_then_remove_on_empty_queue_returns_to_empty(self):
        q = PriorityQueue()
        q.add(7)
        self.assertEqual(len(q), 1)
        q.remove()
        self.assertEqual(len(q), 0)

    def test_one_hundred_adds_and_removes(self):
        q = PriorityQueue()
        items = [i for i in range(100)]
        random.shuffle(items)
        for item in items:
            q.add(item)
        for item in range(100):
            self.assertEqual(q.peek(), item)
            q.remove()

    def test_operation_and_stringification_all_together_because_i_am_lazy(self):
        q = PriorityQueue()
        q.add(8)
        q.add(3)
        self.assertEqual(str(q).replace(' ', ''), '[3,8]')
        q.add(1)
        self.assertEqual(str(q).replace(' ', ''), '[1,8,3]')
        q.remove()
        self.assertEqual(str(q).replace(' ', ''), '[3,8]')

if __name__ == '__main__':
    unittest.main()
