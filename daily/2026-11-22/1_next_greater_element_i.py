# Next Greater Element I — Easy (#496)
# https://leetcode.com/problems/next-greater-element-i/

r"""
The next greater element of a number x in an array is the first number to the right
of x in that array that is greater than x.

You are given two arrays of distinct integers, nums1 and nums2, where nums1 is a
subset of nums2. For each nums1[i], find where that value sits in nums2 and return
its next greater element there, or -1 if there isn't one. Return the answers as a
list in nums1's order.

Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation: In nums2, nothing to the right of 4 is greater, so -1. The first
    number right of 1 that is greater is 3. Nothing right of 2, so -1.

Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]

Constraints:
  - 1 <= nums1.length <= nums2.length <= 1000
  - 0 <= nums1[i], nums2[i] <= 10^4
  - All integers in nums1 and nums2 are unique.
  - All the integers of nums1 also appear in nums2.

Follow-up: can you do it in O(nums1.length + nums2.length) time?"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        raise NotImplementedError


CASES = [
    (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
    (([2, 4], [1, 2, 3, 4]), [3, -1]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().nextGreaterElement, CASES)
