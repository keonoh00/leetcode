# Min Cost Climbing Stairs — Easy (#746)
# https://leetcode.com/problems/min-cost-climbing-stairs/

r"""
You are given an integer array cost, where cost[i] is what you pay to stand on step
i. After paying, you can climb one or two steps. You can start on step 0 or step 1.
Return the minimum total cost to reach the top, which is just past the last step.

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: Start on step 1, pay 15, and climb two steps to the top.

Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: Start on step 0 and step only on the 1s, skipping every 100.
    That's six 1s.

Constraints:
  - 2 <= cost.length <= 1000
  - 0 <= cost[i] <= 999"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev1 = prev2 = 0
        for c in cost:
            current = min(prev1 + c, prev2 + c)
            prev2 = prev1
            prev1 = current
        return min(prev1, prev2)


CASES = [
    (([10, 15, 20],), 15),
    (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().minCostClimbingStairs, CASES)
