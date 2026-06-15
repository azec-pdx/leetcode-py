from doubly_linked_base import _DoublyLinkedBase
from ex import Empty

class LinkedDeque(_DoublyLinkedBase):
    """ Implementation of deque using doubly linked list ADT """

    def first(self):
        """Peek at the front/left of the deque. Return first element but don't remove it"""
        if self.is_empty():
            raise Empty("""Deque is empty""")
        return self._header._next._element

    def last(self):
        """Peek at the back/right of the deque. Return last element but don't remove it"""
        if self.is_empty():
            raise Empty("""Deque is empty""")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Insert new element e at the front/left of the deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Insert new element e at the back/right of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Delete and return the first element at the front/left of the deque."""
        if self.is_empty():
            raise Empty("""Deque is empty""")
        return self.delete_node(self._header._next)

    def delete_last(self):
        """Delete and return the last element at the back/right of the deque."""
        if self.is_empty():
            raise Empty("""Deque is empty""")
        return self.delete_node(self._trailer._prev)
