import sys

sys.path.append("..")  # allows importing everything from utils and adts


class Solution:
    # This is solution of the problem in O(1) extra space complexity.
    # Unlike naive solution, it doesn't store prefix products and suffix products in separate arrays each of which takes O(n) space.
    # (The output array does not count as extra space for space complexity analysis.)

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        size = len(nums)

        answer = [1] * size
        pre = 1
        for i in range(size):
            answer[i] = pre
            pre *= nums[i]

        post = 1
        for j in range(size - 1, -1, -1):
            answer[j] *= post
            post *= nums[j]

        return answer
