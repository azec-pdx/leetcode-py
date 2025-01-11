import sys

sys.path.append("..")  # allows importing everything from utils

from utils.exception_utils import raise_


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]

            if s > target:
                r -= 1
            else:  # s < target
                l += 1

        return []  # empty list in case pair not found
