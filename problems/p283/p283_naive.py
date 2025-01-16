import sys

sys.path.append("..")  # allows importing everything from utils

from utils.exception_utils import raise_

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l]:
                l += 1
            else:
                nums.append(0)
                del nums[l]
                r -= 1
