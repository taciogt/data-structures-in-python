from unittest import TestCase
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_str(self):
        linked_list = LinkedList(1, 2, 3)
        self.assertEqual(str(linked_list), '1->2->3')

        linked_list = LinkedList(1)
        self.assertEqual(str(linked_list), '1')

        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'None')

    def test_equality(self):
        self.assertEqual(LinkedList(), LinkedList())
        self.assertEqual(LinkedList(1), LinkedList(1))
        self.assertEqual(LinkedList(1, 2, 3), LinkedList(1, 2, 3))

        self.assertNotEquals(LinkedList(1, 2, 3), LinkedList())
        self.assertNotEquals(LinkedList(), LinkedList(1, 2, 3))
        self.assertNotEquals(LinkedList(1, 3, 2), LinkedList(1, 2, 3))
        self.assertNotEquals(LinkedList(1, 2, 3), LinkedList(1, 2))
        self.assertNotEquals(LinkedList(1, 2), LinkedList(1, 2, 3))

    def test_length(self):
        pass

    def test_sort(self):
        pass

    def test_del(self):
        pass


class TestLinkedListIndexing(TestCase):
    def test_access_item_by_index(self):
        self.assertEqual(LinkedList('a', 'b', 'c')[0], 'a')
        self.assertEqual(LinkedList('a', 'b', 'c')[1], 'b')
        self.assertEqual(LinkedList('a', 'b', 'c')[2], 'c')

    def test_access_item_with_invalid_index(self):
        with self.assertRaises(IndexError) as context_manager:
            LinkedList('a', 'b', 'c')[4]
        self.assertEqual(str(context_manager.exception), 'LinkedList item is out of range')

    def test_list_slicing(self):
        pass
        # self.assertEqual(str(LinkedList(*range(10))), 'a')
        # self.assertEqual(LinkedList(range(10)), 'a')


