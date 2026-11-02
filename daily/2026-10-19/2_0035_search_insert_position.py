# Search Insert Position — Easy (#35)
# https://leetcode.com/problems/search-insert-position/

r"""
Given a sorted array of distinct integers and a target value, return the index of
target if it is in the array. If it isn't, return the index where it would go to
keep the array sorted. Your algorithm must run in O(log n) time.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
  - 1 <= nums.length <= 10^4
  - -10^4 <= nums[i] <= 10^4
  - nums contains distinct values sorted in ascending order.
  - -10^4 <= target <= 10^4"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = right + 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer


CASES = [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().searchInsert, CASES)
