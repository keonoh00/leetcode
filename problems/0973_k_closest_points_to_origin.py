# K Closest Points to Origin — Medium (#973)
# https://leetcode.com/problems/k-closest-points-to-origin/

r"""
Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y
plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e.,
√(x_1 - x_2)^2 + (y_1 - y_2)^2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg]
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation: The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just
    [[-2,2]].

Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
  - 1 <= k <= points.length <= 10^4
  - -10^4 <= x_i, y_i <= 10^4

Tags: array, math, divide-and-conquer, geometry, sorting, heap-priority-queue,
      quickselect, k-d-tree"""


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        import heapq

        distance_position_heap = []

        for pt in points:
            distance = pt[0] ** 2 + pt[1] ** 2
            heapq.heappush(distance_position_heap, (distance, pt))

        result = []

        for _ in range(k):
            min_val = heapq.heappop(distance_position_heap)
            result.append(min_val[1])

        return result


CASES = [
    (([[1, 3], [-2, 2]], 1), [[-2, 2]]),
    (([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().kClosest, CASES, any_order=True)
