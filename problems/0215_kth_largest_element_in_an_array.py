# Kth Largest Element in an Array — Medium (#215)
# https://leetcode.com/problems/kth-largest-element-in-an-array/

r"""
Given an integer array nums and an integer k, return the k^th largest element in the
array.

Note that it is the k^th largest element in the sorted order, not the k^th distinct
element.

Can you solve it without sorting?

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
  - 1 <= k <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

Tags: array, divide-and-conquer, sorting, heap-priority-queue, quickselect"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq

        nums = [n * -1 for n in nums]

        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1


CASES = [
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().findKthLargest, CASES)
