import sys

sys.path.append("..")  # allows importing everything from utils

from utils.exception_utils import raise_


class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            raise Exception("Intervals array is empty")

        # using list.sort() for inplace sorting of intervals, as more efficient than built-in sorted()
        list.sort(intervals, key=lambda x: x[0] if len(x) == 2 else raise_(ValueError("All intervals should be of size 2!")))
        # altenative without raise_() from utils
        # list.sort(intervals, key=self.sort_func)

        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            last_merged_interval_end = merged_intervals[-1][1]
            if interval[0] <= last_merged_interval_end:
                merged_intervals[-1] = [merged_intervals[-1][0], max(last_merged_interval_end, interval[1])]
            else:
                merged_intervals.append(interval)

        return merged_intervals

    def sort_func(self, x):
        if len(x) == 2:
            x[0]
        raise ValueError("All intervals should be of size 2!")
