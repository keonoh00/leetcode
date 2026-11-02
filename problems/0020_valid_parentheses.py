# Valid Parentheses — Easy (#20)
# https://leetcode.com/problems/valid-parentheses/

r"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.
  - Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Constraints:
  - 1 <= s.length <= 10^4
  - s consists of parentheses only '()[]{}'.

Tags: string, stack, bracket-sequences"""


class Solution:
    def isValid(self, s: str) -> bool:
        conversion_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        open_brackets = []
        for brack in s:
            if brack in conversion_map:
                if (
                    len(open_brackets) == 0
                    or open_brackets[-1] != conversion_map[brack]
                ):
                    return False
                open_brackets.pop()
            else:

                open_brackets.append(brack)

        return len(open_brackets) == 0


CASES = [
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([])",), True),
    (("([)]",), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().isValid, CASES)
