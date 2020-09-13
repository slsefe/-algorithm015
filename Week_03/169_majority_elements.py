"""
leetcode 169 多数元素
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        res, max_cnt = 0, 0
        for k,v in d.items():
            if v > max_cnt:
                res = k
                max_cnt = v
        return res