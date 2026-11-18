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
        week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def isLeap(y: int) -> bool:
            if y % 400 == 0:
                return True
            if y % 100 == 0:
                return False
            return y % 4 == 0

        days = 0
        for y in range(1971, year):
            if isLeap(y):
                days += 366
            else:
                days += 365
        for m in range(month - 1):
            days += monthDays[m]
        if month > 2 and isLeap(year):
            days += 1
        days += day - 1

        return week[(days + 4) % 7]


CASES = [
    ((31, 8, 2019), "Saturday"),
    ((18, 7, 1999), "Sunday"),
    ((15, 8, 1993), "Sunday"),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().dayOfTheWeek, CASES)
