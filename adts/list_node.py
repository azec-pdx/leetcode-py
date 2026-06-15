class ListNode:
    """Lightweight class for storing a node of a singly-linked list.
    Named identical as on Leetcode. Implemented using slots instead of properties.
    """

    __slots__ = "val", "next"

    def __init__(self, val):
        self.val = val
        self.next = None

    # Not part of ADT, just a helper generator to be able to traverse list
    def __iter__(self):
        """
        The generator method that yields all elements one by one.
        Overriding __iter__ makes the object natively iterable.
        """
        current = self
        while current:
            yield current.val
            current = current.next
