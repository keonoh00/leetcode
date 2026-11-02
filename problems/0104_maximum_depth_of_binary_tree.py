# Maximum Depth of Binary Tree — Easy (#104)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

r"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg]
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
  - The number of nodes in the tree is in the range [0, 10^4].
  - -100 <= Node.val <= 100

Tags: tree, depth-first-search, breadth-first-search, binary-tree"""

from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        max_depth = 0

        def getDeep(node: TreeNode | None, depth):
            if not node:
                return
            nonlocal max_depth

            max_depth = max(max_depth, depth)
            getDeep(node.left, depth + 1)
            getDeep(node.right, depth + 1)

        getDeep(root, 1)
        return max_depth


CASES = [
    (([3, 9, 20, None, None, 15, 7],), 3),
    (([1, None, 2],), 2),
]

if __name__ == "__main__":
    from leetcode import TreeNode, build_tree, run

    run(lambda r: Solution().maxDepth(build_tree(r)), CASES)
