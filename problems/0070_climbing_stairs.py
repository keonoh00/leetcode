# Climbing Stairs — Easy (#70)
# https://leetcode.com/problems/climbing-stairs/

r"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb
to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
  - 1 <= n <= 45

Tags: math, dynamic-programming, memoization"""


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2

        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n - 1]


CASES = [
    ((2,), 2),
    ((3,), 3),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().climbStairs, CASES)
