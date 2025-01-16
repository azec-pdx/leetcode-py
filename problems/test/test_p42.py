import unittest

from p42.p42 import Solution


class TestSolution(unittest.TestCase):
    def test_trap(self):
        s = Solution()

        i1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        e1 = 6
        self.assertEqual(s.trap(i1), e1, f"When expecting trapped rain of {e1}")

        i2 = [3, 4, 1, 2, 2, 5, 1, 0, 2]
        e2 = 10
        self.assertEqual(s.trap(i2), e2, f"When expecting trapped rain of {e2}")

        i3 = [4, 2, 0, 3, 2, 5]
        e3 = 9
        self.assertEqual(s.trap(i3), e3, f"When expecting trapped rain of {e3}")
