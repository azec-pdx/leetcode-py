import sys

sys.path.append("..")  # allows importing everything from utils


# Time complexity: O(N)
# Space complexity: O(N)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vals_to_keys = {}

        for i, v in enumerate(nums):
            seek = target - v
            if seek in vals_to_keys:
                return [i, vals_to_keys[seek]]
            vals_to_keys[v] = i

        return []
