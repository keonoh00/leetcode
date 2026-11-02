# Contains Duplicate II — Easy (#219)
# https://leetcode.com/problems/contains-duplicate-ii/

r"""
Given an integer array nums and an integer k, return true if there are two
different indices i and j with nums[i] == nums[j] and abs(i - j) <= k. Otherwise
return false.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9
  - 0 <= k <= 10^5"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        raise NotImplementedError


CASES = [
    (([1, 2, 3, 1], 3), True),
    (([1, 0, 1, 1], 1), True),
    (([1, 2, 3, 1, 2, 3], 2), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().containsNearbyDuplicate, CASES)
