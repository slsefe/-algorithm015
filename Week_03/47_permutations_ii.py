"""
leetcode 47 全排列II
给定一个可包含重复数字的序列，返回所有不重复的全排列
示例：
输入：[1,1,2]
输出：[
        [1,1,2],
        [1,2,1],
        [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, used, res):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, path, used, res)
                    used[i] = False
                    path.pop()

        used = [False] * len(nums)
        nums.sort()
        res = []
        dfs(nums, [], used, res)
        return res
