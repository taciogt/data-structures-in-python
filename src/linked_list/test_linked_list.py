from unittest import TestCase
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_str(self):
        linked_list = LinkedList(1, 2, 3)
        self.assertEqual(str(linked_list), '1->2->3')

        linked_list = LinkedList(1)
        self.assertEqual(str(linked_list), '1')

    def test_access_item_by_index(self):
        self.assertEqual(LinkedList('a', 'b', 'c')[0], 'a')
        self.assertEqual(LinkedList('a', 'b', 'c')[1], 'b')
        self.assertEqual(LinkedList('a', 'b', 'c')[2], 'c')

    def test_access_item_with_invalid_index(self):
        with self.assertRaises(IndexError) as context_manager:
            LinkedList('a', 'b', 'c')[4]
        self.assertEqual(str(context_manager.exception), 'LinkedList item is out of range')
