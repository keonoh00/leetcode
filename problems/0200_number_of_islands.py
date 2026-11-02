# Number of Islands — Medium (#200)
# https://leetcode.com/problems/number-of-islands/

r"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
  - m == grid.length
  - n == grid[i].length
  - 1 <= m, n <= 300
  - grid[i][j] is '0' or '1'.

Tags: array, depth-first-search, breadth-first-search, union-find, matrix"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        lands = set()
        for _y in range(len(grid)):
            for _x in range(len(grid[0])):
                if grid[_y][_x] == "1":
                    lands.add((_x, _y))

        seen = set()
        xHigh = len(grid[0])
        yHigh = len(grid)

        def dfs(location):
            positionX, positionY = location
            up = (positionX, positionY - 1)
            down = (positionX, positionY + 1)
            left = (positionX - 1, positionY)
            right = (positionX + 1, positionY)
            for adj in [up, down, left, right]:
                _x, _y = adj
                if adj in seen:
                    continue
                if not (0 <= _x < xHigh and 0 <= _y < yHigh):
                    continue
                if grid[_y][_x] == "1":
                    seen.add(adj)
                    dfs(adj)

        num_island = 0
        for land in lands:
            if land in seen:
                continue
            seen.add(land)
            dfs(land)
            num_island += 1

        return num_island


CASES = [
    (
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
        ),
        1,
    ),
    (
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
        ),
        3,
    ),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().numIslands, CASES)
