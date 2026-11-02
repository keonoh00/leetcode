# Container With Most Water — Medium (#11)
# https://leetcode.com/problems/container-with-most-water/

r"""
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the i^th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    [diagram:
    https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg]
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array
    [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
    container can contain is 49.

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
  - n == height.length
  - 2 <= n <= 10^5
  - 0 <= height[i] <= 10^4

Tags: array, two-pointers, greedy"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        largest = 0
        i = 0
        j = len(height) - 1
        while i < j:
            x = j - i
            left_height = height[i]
            right_height = height[j]
            if left_height > right_height:
                y = right_height
                j -= 1
            else:
                y = left_height
                i += 1

            area = x * y
            if area > largest:
                largest = area

        return largest


CASES = [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().maxArea, CASES)
