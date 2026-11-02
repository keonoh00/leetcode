# Longest Consecutive Sequence — Medium (#128)
# https://leetcode.com/problems/longest-consecutive-sequence/

r"""
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
    Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Example 3:
    Input: nums = [1,0,1,2]
    Output: 3

Constraints:
  - 0 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        raise NotImplementedError

CASES = [
    (([100, 4, 200, 1, 3, 2],), 4),
    (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
    (([1, 0, 1, 2],), 3),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().longestConsecutive, CASES)
