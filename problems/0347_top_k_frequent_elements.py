# Top K Frequent Elements — Medium (#347)
# https://leetcode.com/problems/top-k-frequent-elements/
# not yet attempted

r"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Example 3:
    Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
    Output: [1,2]

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4
  - k is in the range [1, the number of unique elements in the array].
  - It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where
n is the array's size.

Tags: array, hash-table, divide-and-conquer, sorting, heap-priority-queue, bucket-
      sort, counting, quickselect"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter, defaultdict

        counts = Counter(nums)  # num : number of frequency

        inverted_counts = defaultdict(
            set
        )  # number of frequency : nums with the frequency

        for num, c in counts.items():
            inverted_counts[c].add(num)

        sorted_counts = sorted(
            inverted_counts.keys(), reverse=True
        )  # sorted iterable with counts

        result = []

        for c in sorted_counts:
            result.extend(inverted_counts[c])
            if len(result) == k:
                return result

        return result


CASES = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), [1, 2]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().topKFrequent, CASES, any_order=True)
