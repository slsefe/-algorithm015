"""
leetcode 102 二叉树的层序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            level_queue = []
            level_res = []
            for node in queue:
                level_res.append(node.val)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            res.append(level_res)
            queue = level_queue
        return res
