import unittest

from p238.p238_naive import Solution


class TestSolution(unittest.TestCase):
    def test_productExceptSelf_example1(self):
        s = Solution()

        nums1 = [1, 2, 3, 4]
        ex1 = [24, 12, 8, 6]
        res1 = s.productExceptSelf(nums1)
        self.assertEqual(res1, ex1, f"When expected {ex1}")

    def test_productExceptSelf_example2(self):
        s = Solution()

        nums2 = [-1, 1, 0, -3, 3]
        ex2 = [0, 0, 9, 0, 0]
        res2 = s.productExceptSelf(nums2)
        self.assertEqual(res2, ex2, f"When expected {ex2}")
