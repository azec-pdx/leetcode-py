import unittest

from p125.p125 import Solution


class TestSolution(unittest.TestCase):
    def test_valid_palindrome1(self):
        s = Solution()

        i1 = "A man, a plan, a canal: Panama"
        e1 = True
        self.assertEqual(s.isPalindrome(i1), e1, f"When expected {e1} ")


    def test_valid_palindrome2(self):
        s = Solution()

        i2 = "race a car"
        e2 = False
        self.assertEqual(s.isPalindrome(i2), e2, f"When expected {e2} ")