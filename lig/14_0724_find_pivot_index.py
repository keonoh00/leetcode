# Find Pivot Index — Easy (#724)
# https://leetcode.com/problems/find-pivot-index/

r"""
Given an array of integers nums, find its pivot index: the index where the sum of
all the numbers strictly to its left equals the sum of all the numbers strictly to
its right.

At the left edge the left sum is 0, because there is nothing to the left. The same
goes for the right sum at the right edge.

Return the leftmost pivot index, or -1 if there isn't one.

Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation: The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation: No index meets the condition.

Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation: The pivot index is 0.
    Left sum = 0 (nothing is left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
  - 1 <= nums.length <= 10^4
  - -1000 <= nums[i] <= 1000"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        raise NotImplementedError


CASES = [
    (([1, 7, 3, 6, 5, 6],), 3),
    (([1, 2, 3],), -1),
    (([2, 1, -1],), 0),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().pivotIndex, CASES)
