"""
leetcode 145 二叉树的后序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion
        def helper(root, res):
            if root:
                helper(root.left, res)
                helper(root.right, res)
                res.append(root.val)

        res = []
        helper(root, res)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]