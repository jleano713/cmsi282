import random
import unittest
from priorityqueue import PriorityQueue
from random import shuffle

class TestPriorityQueue(unittest.TestCase):

    def empty_on_construction(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
    
    def size_zero_on_construction(self):
        pq = PriorityQueue()
        self.assertEqual(len(pq), 0)
    
    def no_longer_empty(self):
        pq = PriorityQueue()
        pq.add(1)
        self.assertTrue(not(pq.is_empty()))
        self.assertEqual(len(pq), 1)

    def size_zero_after_removal(self):
        pq = PriorityQueue()
        pq.add(1)
        pq.remove()
        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)

    def enqueueing_0_to_5(self):
        pq = PriorityQueue()
        input_elements = [[i] for i in range(6)]
        shuffle(input_elements)
        for i in input_elements:
            pq.add(i)
        test_elements = [0,1,2,3,4,5]
        elements = []
        for i in range(0, 6):
            elements.append(pq.peek())
            pq.remove()
        self.assertEqual(test_elements, elements)

    def removing_from_an_empty_array(self):
        pq = PriorityQueue()
        with self.assertRaises(RuntimeError):
            pq.remove()

    def peeking_an_empty_array(self):
        pq = PriorityQueue()
        with self.assertRaises(RuntimeError):
            pq.peek()
            




        
