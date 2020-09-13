"""
leetcode 78 子集
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res1 = self.subsets(nums[:-1])
        res = res1 + [_+[nums[-1]] for _ in res1]
        return res