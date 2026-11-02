# Validate Binary Search Tree — Medium (#98)
# https://leetcode.com/problems/validate-binary-search-tree/

r"""
Given the root of a binary tree, determine if it is a valid binary search tree
(BST).

A valid BST is defined as follows:

  - The left subtree of a node contains only nodes with keys strictly less than the
    node's key.
  - The right subtree of a node contains only nodes with keys strictly greater than
    the node's key.
  - Both the left and right subtrees must also be binary search trees.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg]
    Input: root = [2,1,3]
    Output: true

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg]
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
  - The number of nodes in the tree is in the range [1, 10^4].
  - -2^31 <= Node.val <= 2^31 - 1"""

from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        raise NotImplementedError


CASES = [
    (([2, 1, 3],), True),
    (([5, 1, 4, None, None, 3, 6],), False),
]

if __name__ == "__main__":
    from leetcode import TreeNode, build_tree, run

    run(lambda r: Solution().isValidBST(build_tree(r)), CASES)
