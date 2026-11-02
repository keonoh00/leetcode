# Koko Eating Bananas — Medium (#875)
# https://leetcode.com/problems/koko-eating-bananas/

r"""
Koko loves to eat bananas. There are n piles of bananas, the i^th pile has piles[i]
bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some
pile of bananas and eats k bananas from that pile. If the pile has less than k
bananas, she eats all of them instead and will not eat any more bananas during this
hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the
guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4

Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

Constraints:
  - 1 <= piles.length <= 10^4
  - piles.length <= h <= 10^9
  - 1 <= piles[i] <= 10^9

Tags: array, binary-search"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        eatingSpeed = max(piles)
        sumPiles = sum(piles)
        slowestPossibleSpeed = math.ceil(sumPiles / h)

        while slowestPossibleSpeed < eatingSpeed:
            midSpeed = (slowestPossibleSpeed - eatingSpeed) // 2 + eatingSpeed
            totalHour = 0
            for pile in piles:
                hourTakePerPile = math.ceil(pile / midSpeed)
                totalHour += hourTakePerPile
            if totalHour <= h:
                eatingSpeed = midSpeed
            else:
                slowestPossibleSpeed = midSpeed + 1

        return eatingSpeed


CASES = [
    (([3, 6, 7, 11], 8), 4),
    (([30, 11, 23, 4, 20], 5), 30),
    (([30, 11, 23, 4, 20], 6), 23),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().minEatingSpeed, CASES)
