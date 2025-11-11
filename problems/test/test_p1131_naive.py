import unittest

from p1131.p1131_naive import Solution


class TestSolution(unittest.TestCase):
    def test_uniqueLargest(self):
        s = Solution()

        nums1 = [0, 1, 0, 3, 12]

        res1 = s.largestUniqueNumber(nums1)
        self.assertEqual(res1, 12, "When expected 12")

        nums2 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
        res2 = s.largestUniqueNumber(nums2)
        self.assertEqual(res2, 8, "When expected 8")

    def test_edge_cases(self):
        s = Solution()

        nums1 = [1]
        res1 = s.largestUniqueNumber(nums1)
        self.assertEqual(res1, 1, "When expected 1")

        nums2 = [1, 1]
        res2 = s.largestUniqueNumber(nums2)
        self.assertEqual(res2, -1, "When expected -1")
