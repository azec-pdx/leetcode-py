import unittest

from p167.p167 import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        s = Solution()

        # Example 1
        i1 = [2, 7, 11, 15]
        t1 = 9
        e1 = [1, 2]
        s1 = s.twoSum(i1, t1)
        self.assertEqual(sorted(e1), sorted(s1), "Lists should be equal")

        # Example 2
        i2 = [2, 3, 4]
        t2 = 6
        e2 = [1, 3]
        s2 = s.twoSum(i2, t2)
        self.assertEqual(sorted(e2), sorted(s2), "Lists should be equal")

        # Example 3
        i3 = [-1, 0]
        t3 = -1
        e3 = [1, 2]
        s3 = s.twoSum(i3, t3)
        self.assertEqual(sorted(e3), sorted(s3), "Lists should be equal")

        # Example 4
        i4 = [1, 2, 3, 10, 20, 30, 35, 45]
        t4 = 80
        e4 = [7, 8]
        s4 = s.twoSum(i4, t4)
        self.assertEqual(sorted(e4), sorted(s4), "Lists should be equal")

    def test_edge_cases(self):
        s = Solution()

        # Edge 1
        i1 = [-2, -1]
        t1 = -2
        e1 = []
        s1 = s.twoSum(i1, t1)
        self.assertFalse(s1)

        # Edge 2
        i2 = []
        t2 = 5
        e2 = []
        s2 = s.twoSum(i2, t2)
        self.assertFalse(s2)
