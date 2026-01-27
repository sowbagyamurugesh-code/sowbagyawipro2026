'''1. Test Runner

A test runner is a tool that discovers, executes, and manages test cases and displays the test results.
Example: pytest acts as a test runner in Python automation.

2. Test Reports

Test reports provide a summary of test execution showing passed, failed, and skipped test cases along with error details.
They help in analyzing test results and tracking test quality.

3. Configuration Files

Configuration files store environment-specific and reusable settings such as URLs, timeouts, and credentials outside the test code.
They improve maintainability and avoid hardcoding values.'''

from math_utils import multiply

def test_multiply():
    print(multiply(2,3))
    assert multiply(2, 3) == 6
