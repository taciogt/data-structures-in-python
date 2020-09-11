class _NodeIterator:
    def __init__(self, current_node):
        self.current_node = current_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node is not None:
            _next = self.current_node.content
            self.current_node = self.current_node.next
            return _next
        else:
            raise StopIteration


class _Node:
    def __init__(self, content, *next_nodes):
        self._content = content
        try:
            self._next = _Node(next_nodes[0], *next_nodes[1:])
        except IndexError:
            self._next = None

    def __str__(self):
        node_str = f'Node({self._content})'
        if self._next is not None:
            node_str += f'->{self._next}'
        return node_str

    def __eq__(self, other):
        if other is None:
            return False
        return self.content == other.content and self.next == other.next

    def __getitem__(self, item):
        if isinstance(item, slice):
            raise NotImplementedError

        if item == 0:
            return self._content
        elif self.next is not None:
            return self.next[item - 1]
        else:
            raise IndexError('LinkedList item is out of range')

    @property
    def content(self):
        return self._content

    @property
    def next(self):
        return self._next

    def __iter__(self):
        return _NodeIterator(current_node=self)


# https://docs.python.org/3/reference/datamodel.html#emulating-container-types

class LinkedList:

    def __init__(self, *args):
        try:
            self.head = _Node(args[0], *args[1:])
        except IndexError:
            self.head = None

    def __eq__(self, other):
        return self.head == other.head

    def __len__(self):
        length = 0
        try:
            for _ in self.head:
                length += 1
        except TypeError:
            pass
        return length

    def __str__(self):
        if self.head is not None:
            return f'{self.__class__.__name__}[{self.head}]'
        else:
            return f'{self.__class__.__name__}[]'

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if isinstance(item, slice):
            def include_index(index):
                match_step = item.step is None or index % item.step == 0
                should_stop = item.stop is not None and index >= item.stop
                return item.start <= index and match_step and not should_stop

            return LinkedList(*[node for index, node in enumerate(self.head)
                                if include_index(index)])
        if isinstance(item, int):
            return self.head[item]
        raise TypeError(f'{self.__class__.__name__} indices must be integers or slices, not {item.__class__.__name__}')
