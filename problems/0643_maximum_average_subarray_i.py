# Maximum Average Subarray I — Easy (#643)
# https://leetcode.com/problems/maximum-average-subarray-i/

r"""
You are given an integer array nums of n elements and an integer k. Find the
contiguous subarray of length exactly k that has the largest average, and return
that average. Answers within 10^-5 of the true value are accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: The best subarray is [12,-5,-6,50], with average 51 / 4 = 12.75.

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
  - n == nums.length
  - 1 <= k <= n <= 10^5
  - -10^4 <= nums[i] <= 10^4"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        from collections import deque

        stack: deque[int] = deque()

        for i in range(k):
            stack.append(nums[i])

        window_sum = sum(stack)
        largest = window_sum
        i = k
        while i < len(nums):
            window_sum -= stack.popleft()
            stack.append(nums[i])
            window_sum += nums[i]
            if largest < window_sum:
                largest = window_sum
            i += 1

        return largest / k


CASES = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().findMaxAverage, CASES)
