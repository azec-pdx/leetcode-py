import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:

        if len(nums) == 0:
            return None

        elif len(nums) == 1:
            return nums[0]

        nums.sort(reverse=True)
        # print(nums)

        i = 0
        j = 0
        while i < len(nums):
            # print(f"i={i}")
            if (i == len(nums) - 1) and (nums[i-1] > nums[i]): # if i is pointing at the last element and it is different than previous, then it must be unique
                return nums[i]
            else:
                j = i + 1
                # print(f"i={i}, j={j}")
                while j < len(nums)-1 and nums[i] == nums[j]:
                    j += 1
                    # print(f"i={i}, j={j}")
                
                # if j ran all the way to the end and value is same as previous element, then no unique element was found
                if j == len(nums) - 1 and nums[j] == nums[j-1]:
                    return -1
                
                if (j == i + 1) and (nums[i] > nums[j]):
                    return nums[i]
                i = j

