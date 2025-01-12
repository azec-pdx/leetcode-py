import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        rs = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = n + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    rs.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

                    while nums[r + 1] == nums[r] and l < r:
                        r -= 1

        return rs
