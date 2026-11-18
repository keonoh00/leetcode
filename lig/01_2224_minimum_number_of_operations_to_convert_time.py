# Minimum Number of Operations to Convert Time — Easy (#2224)
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

r"""
You are given two 24-hour times as strings, current and correct, each in the form
"HH:MM". In one operation you can add 1, 5, 15 or 60 minutes to current. Return the
smallest number of operations that turns current into correct.

Example 1:
    Input: current = "02:30", correct = "04:35"
    Output: 3
    Explanation: Add 60 minutes to get "03:30", add 60 again to get "04:30", then
    add 5 to get "04:35". It can't be done in fewer than 3 operations.

Example 2:
    Input: current = "11:00", correct = "11:01"
    Output: 1

Constraints:
  - current and correct are in the format "HH:MM".
  - current <= correct"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        raise NotImplementedError


CASES = [
    (("02:30", "04:35"), 3),
    (("11:00", "11:01"), 1),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().convertTime, CASES)
