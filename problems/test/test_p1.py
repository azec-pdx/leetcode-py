import unittest

from p1.p1 import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        s = Solution()

        # Example 1
        i1 = [2, 7, 11, 15]
        t1 = 9
        e1 = [0, 1]
        s1 = s.twoSum(i1, t1)
        self.assertEqual(sorted(e1), sorted(s1), "Lists should be equal")

        # Example 2
        i2 = [3, 2, 4]
        t2 = 6
        e2 = [1, 2]
        s2 = s.twoSum(i2, t2)
        self.assertEqual(sorted(e2), sorted(s2), "Lists should be equal")

        # Example 3
        i3 = [3, 3]
        t3 = 6
        e3 = [0, 1]
        s3 = s.twoSum(i3, t3)
        self.assertEqual(sorted(e3), sorted(s3), "Lists should be equal")

        # Example 4
        i4 = [1, 2, 3]
        t4 = 5
        e4 = [1, 2]
        s4 = s.twoSum(i4, t4)
        self.assertEqual(sorted(e4), sorted(s4), "Lists should be equal")
