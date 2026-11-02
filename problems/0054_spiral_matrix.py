# Spiral Matrix — Medium (#54)
# https://leetcode.com/problems/spiral-matrix/

r"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg]
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg]
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
  - m == matrix.length
  - n == matrix[i].length
  - 1 <= m, n <= 10
  - -100 <= matrix[i][j] <= 100"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        raise NotImplementedError


CASES = [
    (([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().spiralOrder, CASES)
