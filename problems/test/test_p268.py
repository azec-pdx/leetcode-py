import unittest

from p268.p268 import Solution


class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()

        i1 = [3,0,1]
        e1 = 2
        r1 = s.missingNumber(i1)
        self.assertEqual(r1, e1, f"When expected {e1}")

    def test_example2(self):
        s = Solution()

        i2 = [0,1]
        e2 = 2
        r2 = s.missingNumber(i2)
        self.assertEqual(r2, e2, f"When expected {e2}")

    def test_example3(self):
        s = Solution()

        i3 = [9,6,4,2,3,5,7,0,1]
        e3 = 8
        r3 = s.missingNumber(i3)
        self.assertEqual(r3, e3, f"When expected {e3}")
