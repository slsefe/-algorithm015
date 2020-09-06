"""
leetcode 144 二叉树前序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        def helper(root, res):
            if root:
                res.append(root.val)
                if root.left: helper(root.left, res)
                if root.right: helper(root.right, res)
        res = []
        helper(root, res)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration
        if not root: return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res