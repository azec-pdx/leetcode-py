import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = 0
        for r, _ in enumerate(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
