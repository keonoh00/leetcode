"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


# Brute Force Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        for x in range(len(s)):
            char_collection = set()
            for y in range(x, len(s)):
                if s[y] in char_collection:
                    break

                char_collection.add(s[y])
            if len(char_collection) > len(longest):
                longest = char_collection

        return len(longest)


sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
print(sol.lengthOfLongestSubstring(s="bbbbb"))
print(sol.lengthOfLongestSubstring(s=" "))
print(sol.lengthOfLongestSubstring(s="au"))
print(sol.lengthOfLongestSubstring(s="a"))
print(sol.lengthOfLongestSubstring(s="pwwkew"))
