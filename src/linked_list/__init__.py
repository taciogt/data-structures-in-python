class LinkedList:

    def __init__(self, *args):
        self.data = args[0]
        next_args = args[1:]
        self.next = LinkedList(*next_args) if len(next_args) > 0 else None

    def __str__(self):
        if self.next is None:
            return f'{self.data}'
        else:
            return f'{self.data}->{self.next}'

    def __getitem__(self, item):
        if item == 0:
            return self.data
        elif self.next is not None:
            return self.next[item-1]
        else:
            raise IndexError('LinkedList item is out of range')
