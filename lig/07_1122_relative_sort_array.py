# Relative Sort Array — Easy (#1122)
# https://leetcode.com/problems/relative-sort-array/

r"""
You are given two arrays, arr1 and arr2. The values in arr2 are distinct, and every
value in arr2 also appears in arr1.

Sort arr1 so that its values come in the same relative order as in arr2. Values of
arr1 that don't appear in arr2 go at the end, in ascending order.

Example 1:
    Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
    Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
    Output: [22,28,8,6,17,44]

Constraints:
  - 1 <= arr1.length, arr2.length <= 1000
  - 0 <= arr1[i], arr2[i] <= 1000
  - All the values of arr2 are distinct.
  - Each arr2[i] is in arr1."""


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        raise NotImplementedError


CASES = [
    (
        ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    ),
    (([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]), [22, 28, 8, 6, 17, 44]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().relativeSortArray, CASES)
