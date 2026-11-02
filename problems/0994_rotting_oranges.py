# Rotting Oranges — Medium (#994)
# https://leetcode.com/problems/rotting-oranges/

r"""
You are given an m x n grid where each cell can have one of three values:

  - 0 representing an empty cell,
  - 1 representing a fresh orange, or
  - 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2019/02/16/oranges.png]
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never
    rotten, because rotting only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is
    just 0.

Constraints:
  - m == grid.length
  - n == grid[i].length
  - 1 <= m, n <= 10
  - grid[i][j] is 0, 1, or 2.

Tags: array, breadth-first-search, matrix"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from collections import deque

        xHigh = len(grid[0])
        yHigh = len(grid)

        rotten_oranges = deque()
        fresh_oranges = 0
        for _y in range(0, yHigh):
            for _x in range(0, xHigh):
                freshness = grid[_y][_x]
                if freshness == 1:
                    fresh_oranges += 1
                elif freshness == 2:
                    rotten_oranges.append([_x, _y])

        minutes = 0
        while rotten_oranges and fresh_oranges:
            for _ in range(len(rotten_oranges)):
                position = rotten_oranges.popleft()
                positionX, positionY = position

                up = [positionX, positionY - 1]
                down = [positionX, positionY + 1]
                left = [positionX - 1, positionY]
                right = [positionX + 1, positionY]

                for dir in [up, down, left, right]:
                    _x, _y = dir
                    if 0 <= _x < xHigh and 0 <= _y < yHigh:
                        freshness = grid[_y][_x]
                        if freshness == 1:
                            grid[_y][_x] = 2
                            rotten_oranges.append([_x, _y])
                            fresh_oranges -= 1

            minutes += 1

        return -1 if fresh_oranges else minutes


CASES = [
    (([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4),
    (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1),
    (([[0, 2]],), 0),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().orangesRotting, CASES)
