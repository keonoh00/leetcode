# Middle of the Linked List — Easy (#876)
# https://leetcode.com/problems/middle-of-the-linked-list/

r"""
Given the head of a singly linked list, return its middle node. If there are two
middle nodes, return the second one.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node is 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: There are two middle nodes, 3 and 4, so return the second one.

Constraints:
  - The number of nodes in the list is in the range [1, 100].
  - 1 <= Node.val <= 100"""

from __future__ import annotations


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        collection = []
        i = 0

        while head:
            collection.append(head)
            head = head.next
            i += 1

        half_idx = i // 2

        return collection[half_idx]


CASES = [
    (([1, 2, 3, 4, 5],), [3, 4, 5]),
    (([1, 2, 3, 4, 5, 6],), [4, 5, 6]),
]

if __name__ == "__main__":
    # ListNode too, so your code can call ListNode() just as it can on LeetCode.
    from leetcode import ListNode, build_linked_list, linked_list_to_list, run

    run(
        lambda h: linked_list_to_list(Solution().middleNode(build_linked_list(h))),
        CASES,
    )
