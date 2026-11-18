# Remove All Adjacent Duplicates In String — Easy (#1047)
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

r"""
You are given a string s of lowercase English letters. A duplicate removal picks two
adjacent, equal letters and deletes both. Keep making duplicate removals until none
are possible, then return the final string. The answer is always unique.

Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation: Removing "bb" gives "aaca". Removing "aa" then gives "ca", which
    has no adjacent equal letters left.

Example 2:
    Input: s = "azxxzy"
    Output: "ay"

Constraints:
  - 1 <= s.length <= 10^5
  - s consists of lowercase English letters."""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        raise NotImplementedError


CASES = [
    (("abbaca",), "ca"),
    (("azxxzy",), "ay"),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().removeDuplicates, CASES)
