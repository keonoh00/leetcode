# Majority Element — Easy (#169)
# https://leetcode.com/problems/majority-element/

r"""
Given an array nums of size n, return the majority element: the value that appears
more than n / 2 times (rounded down). The majority element always exists.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
  - n == nums.length
  - 1 <= n <= 5 * 10^4
  - -10^9 <= nums[i] <= 10^9

Follow-up: can you solve it in O(n) time and O(1) extra space?"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        raise NotImplementedError


CASES = [
    (([3, 2, 3],), 3),
    (([2, 2, 1, 1, 1, 2, 2],), 2),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().majorityElement, CASES)
