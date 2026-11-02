# Invert Binary Tree — Easy (#226)
# https://leetcode.com/problems/invert-binary-tree/

r"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg]
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    [diagram: https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg]
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
  - The number of nodes in the tree is in the range [0, 100].
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
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(node: TreeNode | None):
            if not node:
                return

            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root


CASES = [
    (([4, 2, 7, 1, 3, 6, 9],), [4, 7, 2, 9, 6, 3, 1]),
    (([2, 1, 3],), [2, 3, 1]),
    (([],), []),
]

if __name__ == "__main__":
    from leetcode import TreeNode, build_tree, run, tree_to_list

    run(lambda r: tree_to_list(Solution().invertTree(build_tree(r))), CASES)
