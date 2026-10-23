import sys

sys.path.append("..")  # allows importing everything from utils and adts


class Solution:
    # This solution uses fixed array of 3 elements to count occurrences for each color, so sorting of any kind is not needed because indices of counter array
    # match the numbers used to indicate colors.
    # In general sense, if this was more colors, but the number of colors is unknown upfront, list/array could not be used, but rather dict instead. In that
    # case, keys of a dict would have to be sorted ascending, in order for second loop to cover all possible flags.

    def sortColors(self, nums: list[int]) -> None:
        ccount = [0] * 3
        # Count total occurrences of each color and store counts
        for v in nums:
            ccount[v] += 1

        index = 0
        for clr in range(3):
            for _ in range(ccount[clr]):
                nums[index] = clr
                index += 1

        return nums
