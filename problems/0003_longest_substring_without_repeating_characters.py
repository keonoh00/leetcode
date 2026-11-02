# Longest Substring Without Repeating Characters — Medium (#3)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

r"""
Given a string s, find the length of the longest substring without duplicate
characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and
    "cab" are also correct answers.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a
    substring.

Constraints:
  - 0 <= s.length <= 10^5
  - s consists of English letters, digits, symbols and spaces.

Tags: hash-table, string, sliding-window"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        window_chars = set()
        for right in range(len(s)):
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left += 1
            window_chars.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


CASES = [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().lengthOfLongestSubstring, CASES)
