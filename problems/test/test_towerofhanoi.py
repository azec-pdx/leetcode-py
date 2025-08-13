import time
import unittest

from towerofhanoi.towerofhanoi_simple import Solution as SimpleSolution


class TestSolution(unittest.TestCase):
    def test_towerofhanoi_simple(self):
        start_time = time.time()

        s = SimpleSolution()

        n = 10

        s.towerofhanoi(n, "A", "B", "C")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time with solution: {elapsed_time} seconds")
