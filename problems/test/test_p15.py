import unittest

from p15.p15 import Solution


class TestSolution(unittest.TestCase):
    def test_threeSum(self):
        s = Solution()

        i1 = [-1, 0, 1, 2, -1, -4]
        e1 = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(s.threeSum(i1), e1, f"When expected {e1} ")

        i2 = [0, 1, 1]
        e2 = []
        self.assertEqual(s.threeSum(i2), e2, f"When expected {e2} ")

        i3 = [0, 0, 0]
        e3 = [[0, 0, 0]]
        self.assertEqual(s.threeSum(i3), e3, f"When expected {e3} ")

        i4 = [0, 0, 0, 0]
        e4 = [[0, 0, 0]]
        self.assertEqual(s.threeSum(i4), e4, f"When expected {e4} ")

        i5 = [-1, 0, 1, 2, -1, -4, -1, -5, -6, -3]
        e5 = [[-3, 1, 2], [-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(s.threeSum(i5), e5, f"When expected {e5} ")

        i6 = [-2, 0, 1, 1, 2]
        e6 = [[-2, 0, 2], [-2, 1, 1]]
        self.assertEqual(s.threeSum(i6), e6, f"When expected {e6} ")

        i7 = [-2,0,0,2,2]
        e7 = [[-2,0,2]]
        self.assertEqual(s.threeSum(i7), e7, f"When expected {e7} ")
