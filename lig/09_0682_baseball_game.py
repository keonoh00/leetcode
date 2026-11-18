# Baseball Game — Easy (#682)
# https://leetcode.com/problems/baseball-game/

r"""
You are keeping score for a baseball game with odd rules. The record starts empty.
You are given a list of strings, operations, and apply them in order. Each one is
one of:

  - An integer x: record a new score of x.
  - "+": record a new score that is the sum of the previous two scores.
  - "D": record a new score that is double the previous score.
  - "C": cancel the previous score, removing it from the record.

Return the sum of all the scores on the record after every operation is applied.
The answer and every value along the way fit in a 32-bit integer, and every
operation is valid.

Example 1:
    Input: operations = ["5","2","C","D","+"]
    Output: 30
    Explanation:
    "5" - record 5, the record is [5]
    "2" - record 2, the record is [5, 2]
    "C" - cancel 2, the record is [5]
    "D" - record 2 * 5 = 10, the record is [5, 10]
    "+" - record 5 + 10 = 15, the record is [5, 10, 15]
    The total is 5 + 10 + 15 = 30.

Example 2:
    Input: operations = ["5","-2","4","C","D","9","+","+"]
    Output: 27
    Explanation:
    "5"  - the record is [5]
    "-2" - the record is [5, -2]
    "4"  - the record is [5, -2, 4]
    "C"  - the record is [5, -2]
    "D"  - the record is [5, -2, -4]
    "9"  - the record is [5, -2, -4, 9]
    "+"  - the record is [5, -2, -4, 9, 5]
    "+"  - the record is [5, -2, -4, 9, 5, 14]
    The total is 5 - 2 - 4 + 9 + 5 + 14 = 27.

Example 3:
    Input: operations = ["1","C"]
    Output: 0

Constraints:
  - 1 <= operations.length <= 1000
  - operations[i] is "C", "D", "+", or an integer in [-3 * 10^4, 3 * 10^4] as a
    string.
  - For "+", there are always at least two previous scores on the record.
  - For "C" and "D", there is always at least one previous score on the record."""


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        raise NotImplementedError


CASES = [
    ((["5", "2", "C", "D", "+"],), 30),
    ((["5", "-2", "4", "C", "D", "9", "+", "+"],), 27),
    ((["1", "C"],), 0),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().calPoints, CASES)
