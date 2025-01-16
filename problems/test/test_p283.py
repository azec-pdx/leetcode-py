import unittest

from p283.p283 import Solution


class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        s = Solution()

        i1 = [0, 1, 0, 3, 12]
        e1 = [1, 3, 12, 0, 0]
        s.moveZeroes(i1)
        self.assertEqual(i1, e1, f"When expected {e1}")

        i1 = [1, 0]
        e1 = [1, 0]
        s.moveZeroes(i1)
        self.assertEqual(i1, e1, f"When expected {e1}")

    def test_edge_cases(self):
        s = Solution()

        i2 = [0]
        e2 = [0]
        s.moveZeroes(i2)
        self.assertEqual(i2, e2, f"When expected {e2}")

        i3 = []
        e3 = []
        s.moveZeroes(i3)
        self.assertEqual(i3, e3, f"When expected {e3}")

        i4 = [1]
        e4 = [1]
        s.moveZeroes(i4)
        self.assertEqual(i4, e4, f"When expected {e4}")
