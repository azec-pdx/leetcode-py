# Uses Python 3.13.0 for type hints and other features
# Might need rework for Leetcode type hints using Python: 3.11.10 (main, Sep  7 2024, 18:35:41) [GCC 13.2.0]

import sys

sys.path.append("..")  # allows importing everything from utils

from utils.exception_utils import raise_


class Solution:
    def maxArea(self, height: list[int]) -> int:
        if not height:
            raise_("height list is empty!")

        i = 0
        j = len(height) - 1
        max_area = 0
        lim = 0
        while i < j:
            if min(height[i], height[j]) >= lim:
                current_area = (j - i) * min(height[i], height[j])
                max_area = max(current_area, max_area)
                lim = min(height[i], height[j])

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return max_area
