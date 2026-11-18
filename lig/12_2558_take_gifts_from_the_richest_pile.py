# Take Gifts From the Richest Pile — Easy (#2558)
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

r"""
You are given an integer array gifts, where gifts[i] is the number of gifts in the
i-th pile. Every second you do the following:

  - Pick the pile with the most gifts. If several piles tie, pick any of them.
  - Leave behind the floor of the square root of the number of gifts in that pile,
    and take the rest.

Return how many gifts are left across all the piles after k seconds.

Example 1:
    Input: gifts = [25,64,9,4,100], k = 4
    Output: 29
    Explanation:
    Second 1: the pile of 100 drops to 10.
    Second 2: the pile of 64 drops to 8.
    Second 3: the pile of 25 drops to 5.
    Second 4: the pile of 10 drops to 3.
    The piles are now [5,8,9,4,3], so 29 gifts are left.

Example 2:
    Input: gifts = [1,1,1,1], k = 4
    Output: 4
    Explanation: The floor of the square root of 1 is 1, so no pile ever changes.

Constraints:
  - 1 <= gifts.length <= 10^3
  - 1 <= gifts[i] <= 10^9
  - 1 <= k <= 10^3"""


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        raise NotImplementedError


CASES = [
    (([25, 64, 9, 4, 100], 4), 29),
    (([1, 1, 1, 1], 4), 4),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().pickGifts, CASES)
