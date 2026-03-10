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
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     merge_sorted = []
    #     i = 0
    #     j = 0
    #     while i <= len(nums1) or j <= len(nums2):
    #         if i >= len(nums1):
    #             merge_sorted.extend(nums2[j::])
    #             break
    #         if j >= len(nums2):
    #             merge_sorted.extend(nums1[i::])
    #             break
    #         if nums1[i] < nums2[j]:
    #             merge_sorted.append(nums1[i])
    #             i += 1
    #         else:
    #             merge_sorted.append(nums2[j])
    #             j += 1

    #     mid = len(merge_sorted) // 2

    #     if len(merge_sorted) % 2 == 0:
    #         return (merge_sorted[mid - 1] + merge_sorted[mid]) / 2
    #     else:
    #         return merge_sorted[mid]

    # Binary Serach Approach
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)
        while True:
            i = (l + r) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


sol = Solution()

print(sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
