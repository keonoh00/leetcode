# Subarray Sum Equals K — Medium (#560)
# https://leetcode.com/problems/subarray-sum-equals-k/

r"""
Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

Constraints:
  - 1 <= nums.length <= 2 * 10^4
  - -1000 <= nums[i] <= 1000
  - -10^7 <= k <= 10^7

Tags: array, hash-table, prefix-sum"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_counts = {0: 1}
        total = 0
        count = 0
        for num in nums:
            total += num
            count += total_counts.get(total - k, 0)
            total_counts[total] = total_counts.get(total, 0) + 1
        return count


CASES = [
    (([1, 1, 1], 2), 2),
    (([1, 2, 3], 3), 2),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().subarraySum, CASES)
