# Remove Nth Node From End of List — Medium (#19)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

r"""
Given the head of a linked list, remove the nth node counting from the end of the
list, and return the head of the result.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg]
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
  - The number of nodes in the list is sz.
  - 1 <= sz <= 30
  - 0 <= Node.val <= 100
  - 1 <= n <= sz

Follow up: Could you do this in one pass?

Tags: linked-list, two-pointers"""

from __future__ import annotations


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        output = ListNode()
        output.next = head
        fast = slow = output
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return output.next


CASES = [
    (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
    (([1], 1), []),
    (([1, 2], 1), [1]),
]

if __name__ == "__main__":
    # ListNode too, so your code can call ListNode() just as it can on LeetCode.
    from leetcode import ListNode, build_linked_list, linked_list_to_list, run

    def call(vals, n):
        head = Solution().removeNthFromEnd(build_linked_list(vals), n)
        return linked_list_to_list(head)

    run(call, CASES)
