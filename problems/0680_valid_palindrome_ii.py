# Valid Palindrome II — Easy (#680)
# https://leetcode.com/problems/valid-palindrome-ii/

r"""
Given a string s, return true if s can be a palindrome after deleting at most one
character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: Delete the "c" (or the "b").

Example 3:
    Input: s = "abc"
    Output: false

Constraints:
  - 1 <= s.length <= 10^5
  - s consists of lowercase English letters."""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                drop_left = s[left + 1 : right + 1]
                if drop_left == drop_left[::-1]:
                    return True

                drop_right = s[left:right]
                if drop_right == drop_right[::-1]:
                    return True

                return False

            left += 1
            right -= 1

        return True


CASES = [
    (("aba",), True),
    (("abca",), True),
    (("abc",), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().validPalindrome, CASES)
