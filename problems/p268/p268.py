import sys

sys.path.append("..")  # allows importing everything from utils and adts


class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        hashset = set(nums)
        for i in range(len(nums) + 1):
            if i not in hashset:
                return i
