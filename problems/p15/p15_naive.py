import sys

sys.path.append("..")  # allows importing everything from utils

from utils.exception_utils import raise_
# Naive O(N^2) time solution


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        rs: list[tuple[int]] = []
        nums.sort()  # Inplace sort
        i = 0
        while i < (len(nums) - 2):
            if zero_sum_tuples := self.twoSum(nums[i + 1 :], nums[i]):
                for tup in zero_sum_tuples:
                    rs.append((nums[i], *tup))
            i += 1

        g = list(set(rs))
        return [list(t) for t in g]

    def twoSum(self, nums: list[int], target: int) -> list[tuple[int]]:
        j, k = 0, len(nums) - 1
        r: list[tuple[int]] = []

        while j < k:
            if nums[j] + nums[k] + target == 0:
                r.append((nums[j], nums[k]))
                # Move j & k, to find more potential pairs that could sum up to target
                j += 1
                k -= 1
            if nums[j] + nums[k] + target > 0:
                k -= 1
            elif nums[j] + nums[k] + target < 0:
                j += 1
        return r
