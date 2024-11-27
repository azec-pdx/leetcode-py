import string
import unittest

from p392 import Solution


class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()
        self.assertTrue(solution.isSubsequence("abc", "ahbgdc"))
        self.assertFalse(solution.isSubsequence("axc", "ahbgdc"))

    def test_isSubsequence_edgeCases(self):
        solution = Solution()
        self.assertTrue(solution.isSubsequence("", "x"))
        self.assertFalse(solution.isSubsequence("x", ""))
        self.assertTrue(solution.isSubsequence("", ""))
        self.assertTrue(solution.isSubsequence("z", string.ascii_lowercase))
