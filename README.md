# leetcode-py
Practice and solutions of Leetcode problems in Python


## Organization

The top-level container for all solutions is `problems` directory. Each problem has its own subdirectory which matches `pXXX` format, where `XXX` are the digits representing problem number on Leetcode. For example `problems/p392` contains solution and tests for [P392](https://leetcode.com/problems/is-subsequence/description/).

Inside each specific problem directory there are following files:
- `pXXX.py`: contains a solution to the problem.
- `test_pXXX.py`: contains unit tests for the solution.


## Running tests

There are many ways how tests can be run, depending on what scope is targeted. Below are just some of the examples.

### From the console

- To run all tests for `p392`, run following:

  ```bash
  cd leetcode-py/problems # problems dir
  python -m unittest discover -v -s test -p "*392*.py"
  ```
  The above should output:
  ```txt
  test_isSubsequence (test_p392.TestSolution.test_isSubsequence) ... ok
  test_isSubsequence_edgeCases (test_p392.TestSolution.test_isSubsequence_edgeCases) ... ok
  
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK
  ```

- To run specific test method for `p392`, run following:

  ```bash
  cd leetcode-py/problems # problems dir
  python -m unittest discover -v -s test -p "*392*.py" -k "isSubsequence"
  ```
 

- To run just edge case tests for all problems, run following:

    
  ```bash
  cd leetcode-py/problems # problems dir
  python -m unittest discover -v -s test -k "edge"
  ```

### From the VS Code

Configure `{project-root}/.vscode/settings.json` with the following:

```json
{
    "python.testing.pytestEnabled": false,
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
    "python.testing.cwd": "${workspaceFolder}",
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./problems/test",
        "-p",
        "*test*.py"
    ],
}
```


To run all tests from VS Code:
- Assume that you opened repo root directory in VS Code (`leetcode-py` is `${workspaceFolder}` and opened in VS Code).
- Right click `problems` directory in VS Code.
- Run command: `Run All Tests`.
- On the bottom of VS Code window, there should be a panel with test results and output.
  ![test-results-tab](img/test-results-tab.png)
- On the left menu-bar there is also an icon for tests. Click on it to see all available options for all discovered tests and to filter through them.
  ![tests-discovered](img/tests-discovered.png)
