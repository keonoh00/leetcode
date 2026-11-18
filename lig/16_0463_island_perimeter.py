# Island Perimeter — Easy (#463)
# https://leetcode.com/problems/island-perimeter/

r"""
You are given a row x col grid that maps land and water: grid[i][j] = 1 is land and
grid[i][j] = 0 is water.

Cells connect horizontally and vertically, not diagonally. Water surrounds the whole
grid, and there is exactly one island: one or more connected land cells. The island
has no lakes, meaning no water inside it that isn't connected to the water around
it. Each cell is a square with side length 1.

Return the perimeter of the island.

Example 1:
    Input: grid = [[0,1,0,0],
                   [1,1,1,0],
                   [0,1,0,0],
                   [1,1,0,0]]
    Output: 16
    Explanation: The island's border is made of 16 unit-length edges.

Example 2:
    Input: grid = [[1]]
    Output: 4

Example 3:
    Input: grid = [[1,0]]
    Output: 4

Constraints:
  - row == grid.length
  - col == grid[i].length
  - 1 <= row, col <= 100
  - grid[i][j] is 0 or 1.
  - There is exactly one island in grid."""


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        raise NotImplementedError


CASES = [
    (([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],), 16),
    (([[1]],), 4),
    (([[1, 0]],), 4),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().islandPerimeter, CASES)
