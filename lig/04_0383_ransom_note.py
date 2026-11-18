# Ransom Note — Easy (#383)
# https://leetcode.com/problems/ransom-note/

r"""
Given two strings, ransomNote and magazine, return true if ransomNote can be built
from the letters of magazine, otherwise false. Each letter in magazine can be used
only once.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
  - 1 <= ransomNote.length, magazine.length <= 10^5
  - ransomNote and magazine consist of lowercase English letters."""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        raise NotImplementedError


CASES = [
    (("a", "b"), False),
    (("aa", "ab"), False),
    (("aa", "aab"), True),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().canConstruct, CASES)
