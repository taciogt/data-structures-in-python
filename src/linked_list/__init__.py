

class LinkedList:

    def __init__(self, *args):
        try:
            self.node = args[0]
        except IndexError:
            self.node = None
        next_args = args[1:]
        self.next = LinkedList(*next_args) if len(next_args) > 0 else None

    def __eq__(self, other):
        if other is None or self.node != other.node:
            return False

        return self.node == other.node and self.next == other.next

    def __len__(self):
        if self.next is not None:
            return 1 + len(self.next)
        else:
            return 1

    def __str__(self):
        if self.next is None:
            return f'{self.node}'
        else:
            return f'{self.node}->{self.next}'

    def __getitem__(self, item):
        if item == 0:
            return self.node
        elif self.next is not None:
            return self.next[item-1]
        else:
            raise IndexError('LinkedList item is out of range')
