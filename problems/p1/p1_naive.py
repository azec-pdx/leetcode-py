import sys

sys.path.append("..")  # allows importing everything from utils


# Time complexity: O(NlogN)
# Space complexity: O(N)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_d = {i: nums[i] for i in range(0, len(nums))}
        # Same dict, sorted by value
        nums_vsorted = dict(sorted(nums_d.items(), key=lambda x: x[1]))
        l, r = 0, len(nums_vsorted) - 1

        nums_vsorted_l = list(nums_vsorted.keys())

        while l < r:
            lk = nums_vsorted_l[l]
            lv = nums_vsorted[lk]
            rk = nums_vsorted_l[r]
            rv = nums_vsorted[rk]

            summ = lv + rv
            if summ == target:
                return [lk, rk]

            if summ > target:
                r -= 1
            else:
                l += 1

        return []
