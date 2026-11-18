# Sort Array by Increasing Frequency — Easy (#1636)
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

r"""
Given an array of integers nums, sort it so that values that appear fewer times come
first. When several values appear the same number of times, put the larger value
first. Return the sorted array.

Example 1:
    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: 3 appears once, 1 appears twice and 2 appears three times.

Example 2:
    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: 2 and 3 both appear twice, so they go in decreasing order.

Example 3:
    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
  - 1 <= nums.length <= 100
  - -100 <= nums[i] <= 100"""


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        from collections import defaultdict

        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1

        def sortKey(num):
            return (dictionary[num], -num)

        return sorted(nums, key=sortKey)


CASES = [
    (([1, 1, 2, 2, 2, 3],), [3, 1, 1, 2, 2, 2]),
    (([2, 3, 1, 3, 2],), [1, 3, 3, 2, 2]),
    (([-1, 1, -6, 4, 5, -6, 1, 4, 1],), [5, -1, 4, 4, -6, -6, 1, 1, 1]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().frequencySort, CASES)
