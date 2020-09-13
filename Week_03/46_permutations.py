"""
leetcode 46 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列
示例：
输入：[1,2,3]
输出：
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, used, path, res):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    dfs(nums, used, path, res)
                    path.pop()
                    used.remove(num)
        res = []
        dfs(nums, set(), [], res)
        return res