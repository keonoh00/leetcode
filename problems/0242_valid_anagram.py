# Valid Anagram — Easy (#242)
# https://leetcode.com/problems/valid-anagram/

r"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
  - 1 <= s.length, t.length <= 5 * 10^4
  - s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

Tags: hash-table, string, sorting"""


class Solution:
    def countStringToDict(self, target: str) -> dict:
        set_target = set(target)
        dict_target = dict.fromkeys(set_target, 0)
        for char_target in target:
            dict_target[char_target] += 1
        return dict_target

    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.countStringToDict(s)
        dict_t = self.countStringToDict(t)
        return dict_s == dict_t


CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().isAnagram, CASES)
