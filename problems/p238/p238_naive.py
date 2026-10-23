import sys

sys.path.append("..")  # allows importing everything from utils and adts


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        size = len(nums)

        # Compute prefix products
        prefix_product = [1] * size
        for i in range(1, size):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        # Compute suffix products
        suffix_product = [1] * size
        for j in range(size - 2, -1, -1):
            suffix_product[j] = suffix_product[j + 1] * nums[j + 1]

        # Compute result array
        answer = [0] * size
        for k in range(0, size):
            answer[k] = prefix_product[k] * suffix_product[k]

        return answer
