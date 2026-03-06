from typing import List, Optional

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_nodes(nodes: List[int]) -> ListNode:
    node = ListNode(nodes[-1], None)
    for node_idx in range(len(nodes) - 1, 0, -1):
        node = ListNode(nodes[node_idx], node)
    return node


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum_collection = []
        carry = 0

        while True:
            if l1 is None and l2 is None and carry == 0:
                break

            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()

            sum = l1.val + l2.val + carry
            if sum >= 10:
                carry = 1
                sum -= 10
            else:
                carry = 0

            sum_collection.append(sum)
            l1 = l1.next
            l2 = l2.next

        # Connecting Nodes
        final = ListNode()
        head = final
        for node_idx in range(len(sum_collection)):
            node_value = sum_collection[node_idx]
            head.val = node_value
            if node_idx != len(sum_collection) - 1:
                head.next = ListNode()
                head = head.next

        return final


sol = Solution()


sol.addTwoNumbers(
    create_list_nodes([2, 4, 3]),
    create_list_nodes([5, 6, 4]),
)
sol.addTwoNumbers(
    create_list_nodes([0]),
    create_list_nodes([0]),
)
sol.addTwoNumbers(
    create_list_nodes([9, 9, 9, 9, 9, 9, 9]),
    create_list_nodes([9, 9, 9, 9]),
)
