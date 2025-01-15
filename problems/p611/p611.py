import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        counter = 0

        for i in range(len(nums) - 1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                # because of sorting we know this is valid:
                # nums[i] + nums[l] > nums[r]
                # nums[i] + nums[r] > nums[l]
                # but not sure about
                if nums[l] + nums[r] > nums[i]:
                    # then all combos of (nums[l] and nums[r] in between also satisfy condition)
                    counter += r - l
                    r -= 1  # validate if holds true for smaller r
                else:
                    l += 1  # increasing left increases chance of sum to be greater than nums[i]

        return counter
