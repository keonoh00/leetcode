# Last Stone Weight — Easy (#1046)
# https://leetcode.com/problems/last-stone-weight/

r"""
You are given an array stones, where stones[i] is the weight of the i-th stone.
Each turn, take the two heaviest stones, with weights x <= y, and smash them:
  - If x == y, both stones are destroyed.
  - If x != y, the x stone is destroyed and the y stone's weight becomes y - x.
Repeat until at most one stone is left. Return its weight, or 0 if none is left.

Example 1:
    Input: stones = [2,7,4,1,8,1]
    Output: 1
    Explanation: Smash 7 and 8 to get 1: [2,4,1,1,1]. Smash 2 and 4 to get 2:
    [2,1,1,1]. Smash 2 and 1 to get 1: [1,1,1]. Smash 1 and 1: [1]. The last
    stone weighs 1.

Example 2:
    Input: stones = [1]
    Output: 1

Constraints:
  - 1 <= stones.length <= 30
  - 1 <= stones[i] <= 1000"""


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq

        heap_stones = [-s for s in stones]

        heapq.heapify(heap_stones)

        while len(heap_stones) > 1:

            max_stone = heapq.heappop(heap_stones) * -1
            next_stone = heapq.heappop(heap_stones) * -1

            max_stone_left = max_stone - next_stone
            if max_stone_left > 0:
                heapq.heappush(heap_stones, max_stone_left * -1)

        if heap_stones:
            return heapq.heappop(heap_stones) * -1
        return 0


CASES = [
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().lastStoneWeight, CASES)
