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
  - s consists of English letters, digits, symbols and spaces."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_container = []
        set_container = set()
        i = 0
        max_length = 0

        while i < len(s):
            current_char = s[i]
            while current_char in set_container:
                set_container.remove(list_container.pop(0))
            list_container.append(current_char)
            set_container.add(current_char)
            if max_length < len(set_container):
                max_length = len(set_container)
            i += 1

        return max_length


CASES = [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().lengthOfLongestSubstring, CASES)
