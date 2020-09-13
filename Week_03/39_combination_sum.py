"""
leetcode 39 组合总和
给定一个无重复元素的数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合
candidates中的数组可以无限制重复被选取
示例1：
输入：candidates = [2,3,6,7], target = [7]
输出：
[
    [2,2,3],
    [7]
]
示例2：
输入：candidates = [2,3,5], target=8
输出：
[
    [2,2,2,2],
    [2,3,3],
    [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, begin, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return
            for i in range(begin, len(nums)):
                path.append(nums[i])
                dfs(nums, target - nums[i], i, path, res)
                path.pop()

        res = []
        dfs(candidates, target, 0, [], res)
        return res
