from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Sized, Iterable, Iterator, Sequence, Union

T = TypeVar('T')


class _NodeIterator(Iterator[T]):
    def __init__(self, current_node: _AbstractNode[T]):
        self.current_node = current_node

    def __iter__(self):
        return self

    def __next__(self) -> T:
        try:
            _next = self.current_node.content
            self.current_node = self.current_node.next
            return _next
        except AttributeError:
            raise StopIteration


class _AbstractNode(Generic[T], Iterable[T], ABC):

    @abstractmethod
    def __eq__(self, other) -> bool:
        ...

    @abstractmethod
    def __getitem__(self, index) -> T:
        ...

    def __iter__(self):
        return _NodeIterator(current_node=self)

    @property
    @abstractmethod
    def content(self) -> T:
        ...

    @property
    @abstractmethod
    def next(self) -> _AbstractNode:
        ...


class _EmptyNode(_AbstractNode):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __eq__(self, other):
        if other == _EmptyNode:
            return True
        return False

    def __getitem__(self, _):
        raise IndexError

    @property
    def content(self):
        raise AttributeError

    @property
    def next(self):
        raise AttributeError


class _Node(_AbstractNode):
    def __init__(self, content: T, *next_nodes: Sequence[T]):
        self._content: T = content
        try:
            self._next: _AbstractNode = _Node(next_nodes[0], *next_nodes[1:])
        except IndexError:
            self._next = _EmptyNode()

    def __eq__(self, other):
        try:
            return self.content == other.content and self.next == other.next
        except AttributeError:
            return False

    def __getitem__(self, index: int) -> T:
        if index == 0:
            return self._content
        else:
            return self.next[index - 1]

    @property
    def content(self):
        return self._content

    @property
    def next(self):
        return self._next


class LinkedList(Sized, Iterable[T]):

    def __init__(self, *args):
        try:
            self.head: _AbstractNode[T] = _Node(args[0], *args[1:])
        except IndexError:
            self.head = _EmptyNode()

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.head == other.head
        return False

    def __len__(self):
        length = 0
        for _ in self.head:
            length += 1
        return length

    def __str__(self) -> str:
        list_contents = ', '.join(map(str, self.head))
        return f'{self.__class__.__name__}[{list_contents}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __getitem__(self, item) -> Union[T, LinkedList]:
        if isinstance(item, slice):
            def include_index(index):
                match_step = item.step is None or index % item.step == 0
                should_stop = item.stop is not None and index >= item.stop
                return item.start <= index and match_step and not should_stop

            if self.head is not None:
                return LinkedList(*[node for index, node in enumerate(self.head)
                                    if include_index(index)])
            else:
                return LinkedList()
        if isinstance(item, int):
            try:
                return self.head[item]
            except IndexError:
                raise IndexError('LinkedList item is out of range')
        raise TypeError(f'{self.__class__.__name__} indices must be integers or slices, not {item.__class__.__name__}')

    def __iter__(self) -> Iterator[T]:
        return _NodeIterator(self.head)
