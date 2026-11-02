# Linked List Cycle — Easy (#141)
# https://leetcode.com/problems/linked-list-cycle/

r"""
Given head, the head of a linked list, return true if the list has a cycle, or
false if it doesn't.

A list has a cycle if you can reach some node again by following next pointers.
The examples describe the cycle with pos, the index of the node that the tail's
next pointer links back to (-1 means no cycle). pos is not passed to your
function; it's only used to build the list.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png]
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: The tail links back to the node at index 1 (0-indexed).

Example 2:
    [diagram:
    https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png]
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: The tail links back to the node at index 0.

Example 3:
    [diagram:
    https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png]
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the list.

Constraints:
  - The number of nodes in the list is in the range [0, 10^4].
  - -10^5 <= Node.val <= 10^5
  - pos is -1 or a valid index in the linked list.

Follow up: Can you solve it using only O(1) extra memory?

Tags: hash-table, linked-list, two-pointers"""

from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        check_hashtable = set()
        while head:
            if head in check_hashtable:
                return True

            check_hashtable.add(head)
            head = head.next
        return False


CASES = [
    (([3, 2, 0, -4], 1), True),
    (([1, 2], 0), True),
    (([1], -1), False),
]

if __name__ == "__main__":
    # ListNode too, so your code can call ListNode() just as it can on LeetCode.
    from leetcode import ListNode, build_linked_list, run

    run(lambda vals, pos: Solution().hasCycle(build_linked_list(vals, pos)), CASES)
