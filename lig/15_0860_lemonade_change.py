# Lemonade Change — Easy (#860)
# https://leetcode.com/problems/lemonade-change/

r"""
At a lemonade stand, each lemonade costs $5. Customers stand in a queue and each buys
one lemonade, in the order given by bills. Each customer pays with a $5, $10 or $20
bill, and you must give back the right change so that each one pays exactly $5. You
start with no change at all.

Given bills, where bills[i] is the bill the i-th customer pays with, return true if
you can give every customer the right change, otherwise false.

Example 1:
    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation: From the first 3 customers you collect three $5 bills. The 4th
    pays $10, so you give back a $5. The 5th pays $20, so you give back a $10 and a
    $5. Everyone got the right change.

Example 2:
    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation: From the first 2 customers you collect two $5 bills. The next 2 pay
    $10 each, and each gets a $5 back. The last pays $20, but you only have two $10
    bills, so you can't give back $15.

Constraints:
  - 1 <= bills.length <= 10^5
  - bills[i] is 5, 10 or 20."""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        raise NotImplementedError


CASES = [
    (([5, 5, 5, 10, 20],), True),
    (([5, 5, 10, 10, 20],), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().lemonadeChange, CASES)
