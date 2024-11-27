# leetcode-py
Practice and solutions of Leetcode problems in Python


## Organization

The top-level container for all solutions is `problems` directory. Each problem has its own subdirectory which matches `pXXX` format, where `XXX` are the digits representing problem number on Leetcode. For example `problems/p392` contains solution and tests for [P392](https://leetcode.com/problems/is-subsequence/description/).

Inside each specific problem directory there are following files:
- `pXXX.py`: contains a solution to the problem.
- `test_pXXX.py`: contains unit tests for the solution.


## Running tests

There are two ways to run all tests for any particular problem.

### From the repo root level

To run all tests for `p392`, run following:

```bash
cd leetcode-py # project root
python -m unittest discover -s problems/p392
```

To run specific methods from problem `p392` test suite:

```bash
cd leetcode-py #project root
# This will match only test_isSubsequence() method from TestSolution class in test_p392.py
python -m unittest -k "test_isSubsequence" discover -s problems/p392
```


### From a problem directory

To run all tests for `p392`, run following:

```bash
cd leetcode-py/problems/p392 # problem dir
python -m unittest
```

To run specific methods from problem `p392` test suite:
```bash
cd leetcode-py/problems/p392 # problem dir
# This will run only test_isSubsequence() method from TestSolution class in test_p392.py
python -m unittest test_p392.TestSolution.test_isSubsequence
```
