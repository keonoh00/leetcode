# Word Pattern — Easy (#290)
# https://leetcode.com/problems/word-pattern/

r"""
Given a pattern and a string s, decide whether s follows the pattern.

"Follows" means a full one-to-one match between the letters of pattern and the
words of s:

  - Each letter maps to exactly one word, and each word maps to exactly one letter.
  - No two letters map to the same word, and no two words map to the same letter.

Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    Explanation: 'a' maps to "dog" and 'b' maps to "cat".

Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

Constraints:
  - 1 <= pattern.length <= 300
  - pattern contains only lowercase English letters.
  - 1 <= s.length <= 3000
  - s contains only lowercase English letters and spaces ' '.
  - s has no leading or trailing spaces.
  - The words in s are separated by a single space."""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = dict()

        s_list = s.split(" ")
        converted_s = ""
        if len(s_list) != len(pattern):
            return False

        for word, pat in zip(s_list, pattern):
            if word not in dictionary:
                if pat in dictionary.values():
                    return False
                else:
                    dictionary[word] = pat
            converted_s += dictionary[word]

        return converted_s == pattern


CASES = [
    (("abba", "dog cat cat dog"), True),
    (("abba", "dog cat cat fish"), False),
    (("aaaa", "dog cat cat dog"), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().wordPattern, CASES)
