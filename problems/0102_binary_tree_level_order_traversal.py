# Binary Tree Level Order Traversal — Medium (#102)
# https://leetcode.com/problems/binary-tree-level-order-traversal/

r"""
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).

Example 1:
    [diagram: https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg]
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []

Constraints:
  - The number of nodes in the tree is in the range [0, 2000].
  - -1000 <= Node.val <= 1000

Tags: tree, breadth-first-search, binary-tree"""

from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque

        container = []

        q: deque[TreeNode] = deque()
        if not root:
            return container

        q.append(root)

        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            container.append(row)

        return container


CASES = [
    (([3, 9, 20, None, None, 15, 7],), [[3], [9, 20], [15, 7]]),
    (([1],), [[1]]),
    (([],), []),
]

if __name__ == "__main__":
    from leetcode import TreeNode, build_tree, run

    run(lambda r: Solution().levelOrder(build_tree(r)), CASES)
