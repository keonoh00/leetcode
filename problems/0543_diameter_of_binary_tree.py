# Diameter of Binary Tree — Easy (#543)
# https://leetcode.com/problems/diameter-of-binary-tree/

r"""
Given the root of a binary tree, return the length of its diameter: the number of
edges on the longest path between any two nodes. The path may or may not pass
through the root.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: The longest paths are 4 -> 2 -> 1 -> 3 and 5 -> 2 -> 1 -> 3,
    each with 3 edges.

Example 2:
    Input: root = [1,2]
    Output: 1

Constraints:
  - The number of nodes in the tree is in the range [1, 10^4].
  - -100 <= Node.val <= 100"""

from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        best = 0

        def dfs(node: TreeNode | None):
            nonlocal best
            if not node:
                return 0
            le = dfs(node.left)
            re = dfs(node.right)
            best = max(best, le + re)
            return max(re, le) + 1

        dfs(root)
        return best


CASES = [
    (([1, 2, 3, 4, 5],), 3),
    (([1, 2],), 1),
]

if __name__ == "__main__":
    from leetcode import TreeNode, build_tree, run

    run(lambda r: Solution().diameterOfBinaryTree(build_tree(r)), CASES)
