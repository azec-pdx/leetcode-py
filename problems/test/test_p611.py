import unittest

from p611.p611 import Solution


class TestSolution(unittest.TestCase):
    def test_triangleNumber(self):
        s = Solution()

        i1 = [2, 2, 3, 4]
        e1 = 3
        self.assertEqual(s.triangleNumber(i1), e1, f"When expected {e1} ")

        i2 = [4,2,3,4]
        e2 = 4
        self.assertEqual(s.triangleNumber(i2), e2, f"When expected {e2} ")
