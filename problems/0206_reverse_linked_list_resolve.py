# Reverse Linked List — Easy (#206)
# https://leetcode.com/problems/reverse-linked-list/

r"""
Given the head of a singly linked list, reverse the list and return the head of
the reversed list.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg]
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg]
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
  - The number of nodes in the list is in the range [0, 5000].
  - -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed with a loop or with recursion. Could you
write both?"""

from __future__ import annotations


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        raise NotImplementedError


CASES = [
    (([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
    (([1, 2],), [2, 1]),
    (([],), []),
]

if __name__ == "__main__":
    # ListNode too, so your code can call ListNode() just as it can on LeetCode.
    from leetcode import ListNode, build_linked_list, linked_list_to_list, run

    run(
        lambda h: linked_list_to_list(Solution().reverseList(build_linked_list(h))),
        CASES,
    )
