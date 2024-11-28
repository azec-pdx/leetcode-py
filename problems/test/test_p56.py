import unittest

from p56.p56 import Solution


class TestSolution(unittest.TestCase):
    def test_merge_intervals_1(self):
        s = Solution()

        i1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
        self.assertEqual(s.merge_intervals(i1), [[1, 6], [8, 10], [15, 18]])

        i2 = [[1, 4], [4, 5]]
        self.assertEqual(s.merge_intervals(i2), [[1, 5]])

        i3 = [[0, 10], [0, 0]]
        self.assertEqual(s.merge_intervals(i3), [[0, 10]])

        i4 = [[-5, 5], [6, 10]]
        self.assertEqual(s.merge_intervals(i4), i4)

        i5 = [[-10, -4], [-3, -1], [-6, -2]]
        self.assertEqual(s.merge_intervals(i5), [[-10, -1]])

    def test_edge_cases(self):
        s = Solution()
        i1 = []
        with self.assertRaises(Exception) as ctx:
            s.merge_intervals(i1)
        self.assertTrue("Intervals array is empty" in str(ctx.exception))

        i2 = [[1, 5], [1]]
        with self.assertRaises(ValueError) as ctx:
            s.merge_intervals(i2)
        self.assertTrue("intervals should be of size 2" in str(ctx.exception))

        i3 = [[]]
        with self.assertRaises(Exception) as ctx:
            s.merge_intervals(i3)
        self.assertTrue("intervals should be of size 2" in str(ctx.exception))
