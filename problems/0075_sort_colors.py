# Sort Colors — Medium (#75)
# https://leetcode.com/problems/sort-colors/

r"""
You are given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.

You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Explanation: The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first,
    then all 1s, then all 2s.

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
    Explanation: The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

Constraints:
  - n == nums.length

1 Follow up: Could you come up with a one-pass algorithm using only constant extra
space?"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        raise NotImplementedError

CASES = [
    (([2, 0, 2, 1, 1, 0],), [0, 0, 1, 1, 2, 2]),
    (([2, 0, 1],), [0, 1, 2]),
]

if __name__ == "__main__":
    from leetcode import run

    def call(nums):
        Solution().sortColors(nums)
        return nums

    run(call, CASES)
