from unittest import TestCase
from linked_list import LinkedList


class TestLinkedList(TestCase):
    def test_str(self):
        linked_list = LinkedList(1, 2, 3)
        self.assertEqual(str(linked_list), '1->2->3')
