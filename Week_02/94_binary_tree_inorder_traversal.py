"""
leetcode 94 二叉树中序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
        res = []
        helper(root, res)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res