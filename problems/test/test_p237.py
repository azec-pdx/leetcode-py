import unittest

from p237.p237 import Solution
from p237.p237_naive import Solution as Naive

from adts.list_node import ListNode


class TestSolution(unittest.TestCase):
    def test_naive(self):

        s = Naive()

        # Create linked-list [4,1,3,5]
        head = ListNode(4)
        head.next = n2 = ListNode(1)
        n2.next = n3 = ListNode(2)
        n3.next = n4 = ListNode(5)
        in_sll = list(head)

        # Call solution
        s.deleteNode(n3)
        out_sll = list(head)

        self.assertTrue(len(out_sll) == len(in_sll) - 1, "Size of output list should be one element less then input list")
        self.assertTrue(2 not in out_sll, "Element with value 2 should be removed from the linked list")

    def test_solution_1(self):

        s = Solution()

        # Create linked-list [4,1,3,5]
        head = ListNode(4)
        head.next = n2 = ListNode(1)
        n2.next = n3 = ListNode(2)
        n3.next = n4 = ListNode(5)
        in_sll = list(head)

        # Call solution
        s.deleteNode(n3)
        out_sll = list(head)

        self.assertTrue(len(out_sll) == len(in_sll) - 1, "Size of output list should be one element less then input list")
        self.assertTrue(2 not in out_sll, "Element with value 2 should be removed from the linked list")

    def test_solution_2(self):

        s = Solution()

        # Create linked-list [4,9]
        head = n1 = ListNode(4)
        head.next = ListNode(9)
        in_sll = list(head)

        # Call solution
        s.deleteNode(n1)
        out_sll = list(head)

        self.assertTrue(len(out_sll) == len(in_sll) - 1, "Size of output list should be one element less then input list")
        self.assertTrue(4 not in out_sll, "Element with value 2 should be removed from the linked list")
