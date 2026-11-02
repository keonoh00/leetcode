# Daily Temperatures — Medium (#739)
# https://leetcode.com/problems/daily-temperatures/

r"""
Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the
i^th day to get a warmer temperature. If there is no future day for which this is
possible, keep answer[i] == 0 instead.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Constraints:
  - 1 <= temperatures.length <= 10^5
  - 30 <= temperatures[i] <= 100

Tags: array, stack, monotonic-stack"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        temps_to_wait = []
        for idx, temp in enumerate(temperatures):
            while len(temps_to_wait) > 0:
                wait = temps_to_wait[-1]
                if wait[0] < temp:
                    output[wait[1]] = idx - wait[1]
                    temps_to_wait.pop()
                else:
                    break

            temps_to_wait.append((temp, idx))

        return output


CASES = [
    (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
    (([30, 40, 50, 60],), [1, 1, 1, 0]),
    (([30, 60, 90],), [1, 1, 0]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().dailyTemperatures, CASES)
