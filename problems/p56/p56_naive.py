import math
import sys

sys.path.append("..")  # allows importing everything from utils


class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            raise Exception("Intervals array is empty")

        min_start_all_intervals = min(intervals, key=lambda x: x[0])
        print(f"min_start_all_intervals:{min_start_all_intervals}")

        merged_intervals = [min_start_all_intervals]
        evaluated_min_intervals = [min_start_all_intervals]

        min_interval = min(intervals, key=lambda x: x[0] if x not in evaluated_min_intervals else math.inf)
        while min_interval and len(evaluated_min_intervals) < len(intervals):
            last_merged_interval_end = merged_intervals[-1][1]
            if min_interval[0] <= last_merged_interval_end:
                merged_intervals[-1] = [merged_intervals[-1][0], max(last_merged_interval_end, min_interval[1])]
            else:
                merged_intervals.append(min_interval)

            evaluated_min_intervals.append(min_interval)
            min_interval = min(intervals, key=lambda x: x[0] if x not in evaluated_min_intervals else math.inf)

        print(f"merged_intervals:{merged_intervals}")
        return merged_intervals
