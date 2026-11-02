# Merge Intervals — Medium (#56)
# https://leetcode.com/problems/merge-intervals/

r"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all
overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
    Input: intervals = [[4,7],[1,4]]
    Output: [[1,7]]
    Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
  - 1 <= intervals.length <= 10^4
  - intervals[i].length == 2
  - 0 <= start_i <= end_i <= 10^4"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:  # overlaps the last one
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged


CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[4, 7], [1, 4]],), [[1, 7]]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().merge, CASES)
