# 3Sum — Medium (#15)
# https://leetcode.com/problems/3sum/

r"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not
    matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
  - 3 <= nums.length <= 3000
  - -10^5 <= nums[i] <= 10^5

Tags: array, two-pointers, sorting"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        container = []

        for starting in range(len(sorted_nums) - 2):
            if starting > 0 and sorted_nums[starting] == sorted_nums[starting - 1]:
                continue

            num_1 = sorted_nums[starting]
            i = starting + 1
            j = len(sorted_nums) - 1

            while i < j:
                num_2 = sorted_nums[i]
                num_3 = sorted_nums[j]
                added = num_1 + num_2 + num_3
                if added == 0:
                    container.append([num_1, num_2, num_3])
                    j -= 1
                    while i < j and sorted_nums[i] == num_2:
                        i += 1
                elif added < 0:
                    i += 1
                else:
                    j -= 1

        return container


CASES = [
    (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    (([0, 1, 1],), []),
    (([0, 0, 0],), [[0, 0, 0]]),
    (([-100, -70, -60, 110, 120, 130, 160],), [[-100, -60, 160], [-70, -60, 130]]),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().threeSum, CASES, any_order=True)
