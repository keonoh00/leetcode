# Determine if Two Events Have Conflict — Easy (#2446)
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

r"""
You are given two events that happen on the same day:

  - event1 = [startTime1, endTime1]
  - event2 = [startTime2, endTime2]

Times are 24-hour strings in the form "HH:MM", and both ends of an event are
included. Two events conflict when some moment falls inside both of them. Return
true if the events conflict, otherwise false.

Example 1:
    Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
    Output: true
    Explanation: Both events include 02:00.

Example 2:
    Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
    Output: true
    Explanation: Both events include everything from 01:20 to 02:00.

Example 3:
    Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
    Output: false
    Explanation: The events share no moment.

Constraints:
  - event1.length == event2.length == 2
  - event1[i].length == event2[i].length == 5
  - startTime1 <= endTime1
  - startTime2 <= endTime2
  - All times are in the format "HH:MM"."""


class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        raise NotImplementedError


CASES = [
    ((["01:15", "02:00"], ["02:00", "03:00"]), True),
    ((["01:00", "02:00"], ["01:20", "03:00"]), True),
    ((["10:00", "11:00"], ["14:00", "15:00"]), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().haveConflict, CASES)
