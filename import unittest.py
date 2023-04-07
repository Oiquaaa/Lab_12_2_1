import unittest
from lab12_2_1 import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.llist = LinkedList()
        self.llist.insert_at_end(1)
        self.llist.insert_at_end(2)
        self.llist.insert_at_end(3)
        self.llist.insert_at_end(4)
        self.llist.insert_at_end(5)
        self.llist.insert_at_end(6)

    def test_insert_before_value(self):
        self.llist.insert_before_value(1, 8)
        self.assertEqual(self.llist.head.data, 8)

        self.llist.insert_before_value(3, 6)
        self.assertEqual(self.llist.head.next.next.next.data, 6)

        self.llist.insert_before_value(5, 9)
        self.assertEqual(self.llist.head.next.next.next.next.next.next.data, 9)

if __name__ == '__main__':
    unittest.main()
