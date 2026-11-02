# Valid Palindrome — Easy (#125)
# https://leetcode.com/problems/valid-palindrome/

r"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
  - 1 <= s.length <= 2 * 10^5
  - s consists only of printable ASCII characters.

Tags: two-pointers, string"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            left_char = s[i]
            right_char = s[j]
            if not left_char.isalnum():
                i += 1
                continue
            if not right_char.isalnum():
                j -= 1
                continue

            if left_char.lower() != right_char.lower():
                return False
            i += 1
            j -= 1
        return True


CASES = [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    ((" ",), True),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().isPalindrome, CASES)
