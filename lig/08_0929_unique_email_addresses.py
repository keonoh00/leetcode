# Unique Email Addresses — Easy (#929)
# https://leetcode.com/problems/unique-email-addresses/

r"""
Every valid email address has a local name and a domain name, separated by '@'.
Besides lowercase letters, an address may contain '.' or '+'. For example, in
"alice@leetcode.com", "alice" is the local name and "leetcode.com" is the domain
name.

Two rules apply to the local name only, never to the domain name:

  - Periods are ignored. "alice.z@leetcode.com" and "alicez@leetcode.com" reach the
    same inbox.
  - Everything after the first '+' is ignored. "m.y+name@email.com" reaches
    "my@email.com".

Both rules can apply to the same address.

You send one email to each address in emails. Return how many different addresses
actually receive mail.

Example 1:
    Input: emails = ["test.email+alex@leetcode.com",
                     "test.e.mail+bob.cathy@leetcode.com",
                     "testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" receive
    mail.

Example 2:
    Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    Output: 3

Constraints:
  - 1 <= emails.length <= 100
  - 1 <= emails[i].length <= 100
  - emails[i] consists of lowercase English letters, '+', '.' and '@'.
  - Each emails[i] contains exactly one '@'.
  - All local and domain names are non-empty.
  - Local names do not start with a '+'.
  - Domain names end with ".com" and have at least one character before it."""


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        raise NotImplementedError


CASES = [
    (
        (
            [
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ],
        ),
        2,
    ),
    ((["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"],), 3),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().numUniqueEmails, CASES)
