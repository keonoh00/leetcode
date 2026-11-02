# Two Sum — Easy (#1)
# https://leetcode.com/problems/two-sum/

r"""
Given an array of integers nums and an integer target, return the indices of the
two numbers that add up to target. Each input has exactly one answer, and you may
not use the same element twice. Return the two indices in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - -10^9 <= target <= 10^9
  - Exactly one valid answer exists."""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        collection = dict()
        for x in range(len(nums)):
            pair = target - nums[x]
            if pair in collection:
                return [collection[pair], x]
            else:
                collection[nums[x]] = x


CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().twoSum, CASES, any_order=True)
