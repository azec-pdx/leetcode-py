import unittest

from p11.p11 import Solution


class TestSolution(unittest.TestCase):
    def test_max_area(self):
        s = Solution()

        i1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(s.maxArea(i1), 49, "When expected 49")

        i2 = [1, 1]
        self.assertEqual(s.maxArea(i2), 1, "When expected 1")

        i3 = [1, 7, 30, 25, 7, 1]
        self.assertEqual(s.maxArea(i3), 25, "When expected 25")
