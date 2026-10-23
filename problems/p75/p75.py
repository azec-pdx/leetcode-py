import sys

sys.path.append("..")  # allows importing everything from utils and adts


class Solution:
    # This solution uses Three Pointers pattern.
    # Low (l) pointer shows where next 0 should be
    # Mid (m) pointer iterates over the next elements
    # High (h) pointer shows where next 2 should be
    # When 0 is found by mid, it is swapped with value pointed by low, both mid and low move forward
    # When 1 is found by mid, it is not swapped, it is expected to be there, only mid moves forward
    # When 2 is found by mid, it is swapped with value pointed by high. The swapped value could be any number
    # so mid doesn't move as that value still needs to be examined, but high moves backwards

    def sortColors(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        l, m, h = 0, 0, len(nums) - 1
        while m <= h:
            if nums[m] == 0:
                # Swap 0s found by mid in place of current low
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                # Leave 1s in place
                m += 1
            else:  # 2
                # Swap 2s in place of current high
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
                # Don't touch mid because swapped element could have been either 0 or 2, so it still needs to be processed
        return nums
