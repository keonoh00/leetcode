# House Robber — Medium (#198)
# https://leetcode.com/problems/house-robber/

r"""
You are a professional robber planning to rob houses along a street. Each house has
a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will
automatically contact the police if two adjacent houses were broken into on the same
night.

Given an integer array nums representing the amount of money of each house, return
the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
    (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
  - 1 <= nums.length <= 100
  - 0 <= nums[i] <= 400

Tags: array, dynamic-programming"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best_robs = [nums[0], max(nums[0], nums[1])]

        for idx in range(2, len(nums)):
            money = nums[idx]
            best_robs_so_far = max(best_robs[idx - 1], money + best_robs[idx - 2])
            best_robs.append(best_robs_so_far)

        return best_robs[-1]


CASES = [
    (([1, 2, 3, 1],), 4),
    (([2, 7, 9, 3, 1],), 12),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().rob, CASES)
