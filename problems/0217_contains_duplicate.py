# Contains Duplicate — Easy (#217)
# https://leetcode.com/problems/contains-duplicate/

r"""
Given an integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: All elements are distinct.

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9

Tags: array, hash-table, sorting"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set(nums)
        return len(seen) != len(nums)


CASES = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().containsDuplicate, CASES)
