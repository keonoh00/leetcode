# Find Smallest Letter Greater Than Target — Easy (#744)
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

r"""
You are given an array of characters, letters, sorted in non-decreasing order, and a
character target. letters has at least two different characters.

Return the smallest character in letters that is lexicographically greater than
target. If there is no such character, return the first character in letters.

Example 1:
    Input: letters = ["c","f","j"], target = "a"
    Output: "c"
    Explanation: "c" is the smallest letter in letters greater than "a".

Example 2:
    Input: letters = ["c","f","j"], target = "c"
    Output: "f"
    Explanation: "f" is the smallest letter in letters greater than "c".

Example 3:
    Input: letters = ["x","x","y","y"], target = "z"
    Output: "x"
    Explanation: No letter in letters is greater than "z", so return letters[0].

Constraints:
  - 2 <= letters.length <= 10^4
  - letters[i] is a lowercase English letter.
  - letters is sorted in non-decreasing order.
  - letters contains at least two different characters.
  - target is a lowercase English letter."""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        raise NotImplementedError


CASES = [
    ((["c", "f", "j"], "a"), "c"),
    ((["c", "f", "j"], "c"), "f"),
    ((["x", "x", "y", "y"], "z"), "x"),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().nextGreatestLetter, CASES)
