class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""

        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev_element, next_element):
            self._element = element
            self._prev = prev_element
            self._next = next_element

    def __init__(self):
        """Create an empty list"""
        # Sentinels (dummy nodes) used at the ends of the list
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of the elements in the dll"""
        return self._size

    def is_empty(self):
        """Return True if dll is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        element = node._element
        # help garbage collector
        node._element = node._prev = node._next = None

        return element
