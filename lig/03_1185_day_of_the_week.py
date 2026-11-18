# Day of the Week — Easy (#1185)
# https://leetcode.com/problems/day-of-the-week/

r"""
Given a date as three integers, day, month and year, return the day of the week it
falls on, as one of "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
or "Saturday".

Example 1:
    Input: day = 31, month = 8, year = 2019
    Output: "Saturday"

Example 2:
    Input: day = 18, month = 7, year = 1999
    Output: "Sunday"

Example 3:
    Input: day = 15, month = 8, year = 1993
    Output: "Sunday"

Constraints:
  - The given date is a valid date between the years 1971 and 2100."""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        raise NotImplementedError


CASES = [
    ((31, 8, 2019), "Saturday"),
    ((18, 7, 1999), "Sunday"),
    ((15, 8, 1993), "Sunday"),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().dayOfTheWeek, CASES)
