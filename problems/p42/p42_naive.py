import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = l + 1

        total_rain = 0

        while l < len(height) and r < len(height):
            partial_rain = 0

            while r < len(height) and height[r] < height[l]:
                partial_rain += height[l] - height[r]
                r += 1

            if r < len(height):  # right wall found that can trap rain before r reaching end
                total_rain += partial_rain
                l = r
                r = l + 1

        # print(f"Rain after 1st loop: {total_rain}")

        llim, r, l = l, len(height) - 1, len(height) - 2

        while r > llim and l > llim:
            partial_rain = 0

            while l > llim and height[l] < height[r]:
                partial_rain += height[r] - height[l]
                l -= 1

            if l >= llim:
                total_rain += partial_rain
                r = l
                l = r - 1

        # print(f"Rain after 2nd loop: {total_rain}")

        return total_rain
