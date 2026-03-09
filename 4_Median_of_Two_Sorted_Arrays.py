from typing import List

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    # Two Pointer Brute Force Approach
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_sorted = []
        i = 0
        j = 0
        while i <= len(nums1) or j <= len(nums2):
            if i >= len(nums1):
                merge_sorted.extend(nums2[j::])
                break
            if j >= len(nums2):
                merge_sorted.extend(nums1[i::])
                break
            if nums1[i] < nums2[j]:
                merge_sorted.append(nums1[i])
                i += 1
            else:
                merge_sorted.append(nums2[j])
                j += 1

        mid = len(merge_sorted) // 2

        if len(merge_sorted) % 2 == 0:
            return (merge_sorted[mid - 1] + merge_sorted[mid]) / 2
        else:
            return merge_sorted[mid]


sol = Solution()

print(sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
