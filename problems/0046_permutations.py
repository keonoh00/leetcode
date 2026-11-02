# Permutations — Medium (#46)
# https://leetcode.com/problems/permutations/

r"""
Given an array nums of distinct integers, return all the possible permutations. You
can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
  - 1 <= nums.length <= 6
  - -10 <= nums[i] <= 10
  - All the integers of nums are unique."""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        raise NotImplementedError


CASES = [
    (([1, 2, 3],), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    (([0, 1],), [[0, 1], [1, 0]]),
    (([1],), [[1]]),
]

if __name__ == "__main__":
    from leetcode import run

    # Sort only the outer list: inside a permutation, the order is the answer.
    run(lambda nums: sorted(Solution().permute(nums)), CASES)
