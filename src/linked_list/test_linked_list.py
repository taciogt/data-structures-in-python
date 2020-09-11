from unittest import TestCase, skip
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_str(self):
        linked_list = LinkedList(1, 2, 3)
        self.assertEqual(str(linked_list), 'LinkedList[Node(1)->Node(2)->Node(3)]')

        linked_list = LinkedList(1)
        self.assertEqual(str(linked_list), 'LinkedList[Node(1)]')

        linked_list = LinkedList()
        self.assertEqual(str(linked_list), 'LinkedList[]')

        linked_list = LinkedList(None)
        self.assertEqual(str(linked_list), 'LinkedList[Node(None)]')

    def test_equality(self):
        self.assertEqual(LinkedList(), LinkedList())
        self.assertEqual(LinkedList(1), LinkedList(1))
        self.assertEqual(LinkedList(1, 2, 3), LinkedList(1, 2, 3))

        self.assertNotEqual(LinkedList(1, 2, 3), LinkedList())
        self.assertNotEqual(LinkedList(), LinkedList(1, 2, 3))
        self.assertNotEqual(LinkedList(1, 3, 2), LinkedList(1, 2, 3))
        self.assertNotEqual(LinkedList(1, 2, 3), LinkedList(1, 2))
        self.assertNotEqual(LinkedList(1, 2), LinkedList(1, 2, 3))

    def test_length(self):
        self.assertEqual(0, len(LinkedList()))
        self.assertEqual(1, len(LinkedList(1)))
        self.assertEqual(2, len(LinkedList(1, 2)))
        self.assertEqual(3, len(LinkedList(1, 2, 3)))

    def test_sort(self):
        pass

    def test_del(self):
        pass


class TestLinkedListIndexing(TestCase):
    def test_access_item_by_index(self):
        self.assertEqual(LinkedList('a', 'b', 'c')[0], 'a')
        self.assertEqual(LinkedList('a', 'b', 'c')[1], 'b')
        self.assertEqual(LinkedList('a', 'b', 'c')[2], 'c')

    def test_list_slicing(self):
        linked_list = LinkedList(*range(11))  # LinkedList(1, 2, ... 10)

        self.assertEqual(linked_list[3:6], LinkedList(3, 4, 5))
        self.assertEqual(linked_list[8:], LinkedList(8, 9, 10))
        self.assertEqual(linked_list[0:8:3], LinkedList(0, 3, 6))

    def test_access_item_with_invalid_index(self):
        with self.assertRaises(IndexError) as context_manager:
            _ = LinkedList('a', 'b', 'c')[4]
        self.assertEqual(str(context_manager.exception), 'LinkedList item is out of range')

    def test_invalid_type(self):
        with self.assertRaises(TypeError) as context_manager:
            _ = LinkedList(1, 2)['a']
        self.assertEqual(str(context_manager.exception), 'LinkedList indices must be integers or slices, not str')
