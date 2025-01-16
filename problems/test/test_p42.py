import time
import unittest

from p42.p42 import Solution as Solution
from p42.p42_naive import Solution as NaiveSolution


class TestSolution(unittest.TestCase):
    def test_trap(self):
        start_time = time.time()

        s = Solution()

        i1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        e1 = 6
        self.assertEqual(s.trap(i1), e1, f"When expecting trapped rain of {e1}")

        i2 = [3, 4, 1, 2, 2, 5, 1, 0, 2]
        e2 = 10
        self.assertEqual(s.trap(i2), e2, f"When expecting trapped rain of {e2}")

        i3 = [4, 2, 0, 3, 2, 5]
        e3 = 9
        self.assertEqual(s.trap(i3), e3, f"When expecting trapped rain of {e3}")

        i4 = [
            2,
            5,
            10,
            505,
            1000,
            3000,
            510,
            250,
            221,
            100,
            108,
            44,
            88,
            78,
            79,
            1001,
            2002,
            2019,
            2018,
            2017,
            2016,
            2015,
            2014,
            2020,
            2021,
            2023,
            2024,
            2025,
            2014,
            19999,
            1009,
            2021,
            5,
            2000,
            2,
            5,
            10,
            505,
            1000,
            3000,
            510,
            250,
            221,
            100,
            108,
            44,
            88,
            78,
            79,
            1001,
            2002,
            2019,
            2018,
            2017,
            2016,
            2015,
            2014,
            2020,
            2021,
            2023,
            2024,
            2025,
            2014,
            19999,
            1009,
            2021,
            5,
            2000,
        ]
        e4 = 665003
        self.assertEqual(s.trap(i4), e4, f"When expecting trapped rain of {e4}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time with solution: {elapsed_time} seconds")

    def test_trap_naive(self):
        start_time = time.time()

        s = NaiveSolution()

        i1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        e1 = 6
        self.assertEqual(s.trap(i1), e1, f"When expecting trapped rain of {e1}")

        i2 = [3, 4, 1, 2, 2, 5, 1, 0, 2]
        e2 = 10
        self.assertEqual(s.trap(i2), e2, f"When expecting trapped rain of {e2}")

        i3 = [4, 2, 0, 3, 2, 5]
        e3 = 9
        self.assertEqual(s.trap(i3), e3, f"When expecting trapped rain of {e3}")

        i4 = [
            2,
            5,
            10,
            505,
            1000,
            3000,
            510,
            250,
            221,
            100,
            108,
            44,
            88,
            78,
            79,
            1001,
            2002,
            2019,
            2018,
            2017,
            2016,
            2015,
            2014,
            2020,
            2021,
            2023,
            2024,
            2025,
            2014,
            19999,
            1009,
            2021,
            5,
            2000,
            2,
            5,
            10,
            505,
            1000,
            3000,
            510,
            250,
            221,
            100,
            108,
            44,
            88,
            78,
            79,
            1001,
            2002,
            2019,
            2018,
            2017,
            2016,
            2015,
            2014,
            2020,
            2021,
            2023,
            2024,
            2025,
            2014,
            19999,
            1009,
            2021,
            5,
            2000,
        ]
        e4 = 665003
        self.assertEqual(s.trap(i4), e4, f"When expecting trapped rain of {e4}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time with naive solution: {elapsed_time} seconds")
