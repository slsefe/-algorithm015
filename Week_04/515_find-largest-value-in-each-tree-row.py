"""
leetcode 515 在每个树行中找到最大值
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues_1(self, root: TreeNode) -> List[int]:
        # BFS, 2 queues
        if not root: return []
        queue = [root]
        res = []
        while queue:
            level_max = float('-inf')
            level_queue = []
            for node in queue:
                level_max = max(level_max, node.val)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            res.append(level_max)
            queue = level_queue
        return res

    def largestValues_2(self, root: TreeNode) -> List[int]:
        # BFS, one queue
        from collections import deque
        if not root: return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level_max = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level_max)
        return res
