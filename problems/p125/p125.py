import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not ss[left].isalnum():
                left += 1
            while left < right and not ss[right].isalnum():
                right -= 1

            if ss[left] != ss[right]:
                return False
            left += 1
            right -= 1

        return True
