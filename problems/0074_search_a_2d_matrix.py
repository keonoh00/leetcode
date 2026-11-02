# Search a 2D Matrix — Medium (#74)
# https://leetcode.com/problems/search-a-2d-matrix/

r"""
You are given an m x n integer matrix matrix with the following two properties:

  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the previous
    row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/10/05/mat.jpg]
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg]
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
  - m == matrix.length
  - n == matrix[i].length
  - 1 <= m, n <= 100
  - -10^4 <= matrix[i][j], target <= 10^4

Tags: array, binary-search, matrix"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        smaller_row_idx = 0
        larger_row_idx = len(matrix) - 1
        row_candiate = None
        while smaller_row_idx < larger_row_idx:
            gap = (larger_row_idx - smaller_row_idx) // 2
            mid_row_idx = smaller_row_idx + gap
            mid_row = matrix[mid_row_idx]
            if mid_row[0] <= target and mid_row[-1] >= target:
                row_candiate = mid_row
                break
            elif mid_row[0] > target:
                larger_row_idx = mid_row_idx
            elif mid_row[-1] < target:
                smaller_row_idx = mid_row_idx + 1

        if not row_candiate:
            row_candiate = matrix[smaller_row_idx]
        smaller_column_idx = 0
        larger_column_idx = len(row_candiate)

        while smaller_column_idx < larger_column_idx:
            gap = (larger_column_idx - smaller_column_idx) // 2
            mid_col_idx = smaller_column_idx + gap
            mid_num = row_candiate[mid_col_idx]
            if mid_num >= target:
                larger_column_idx = mid_col_idx
            else:
                smaller_column_idx = mid_col_idx + 1

        if smaller_column_idx < len(row_candiate):
            return row_candiate[smaller_column_idx] == target
        return False


CASES = [
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
    (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().searchMatrix, CASES)
