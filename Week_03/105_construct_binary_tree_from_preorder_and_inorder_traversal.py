"""
leetcode 105 从前序遍历和中序遍历序列构造二叉树
你可以假设树中没有重复的元素
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序遍历：root->left->right
        # 中序遍历：left->root->right
        # 1. 递归终止条件
        if len(preorder) == 0:
            return None
        # 2. 当前层逻辑
        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        # 3. 下探，合并子问题结果
        root.left = self.buildTree(preorder[:idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx:], inorder[idx+1:])
        # 4. 如果需要，重置状态
        return root