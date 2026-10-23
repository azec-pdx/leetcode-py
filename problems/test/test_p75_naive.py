import unittest

from p75.p75_naive import Solution


class TestSolution(unittest.TestCase):
    def test_sortColors_example1(self):
        s = Solution()

        nums1 = [2, 0, 2, 1, 1, 0]
        ex1 = [0, 0, 1, 1, 2, 2]
        res1 = s.sortColors(nums1)
        self.assertEqual(res1, ex1, f"When expected {ex1}")

    def test_sortColors_example2(self):
        s = Solution()

        nums2 = [2, 0, 1]
        ex2 = [0, 1, 2]
        res2 = s.sortColors(nums2)
        self.assertEqual(res2, ex2, f"When expected {ex2}")
