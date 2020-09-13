"""
leetcode 77 组合
给定两个整数n和k，返回1...n中所有可能的k个数的组合
示例：
输入：n = 4, k = 2
输出：
[
    [1,2],
    [1,3],
    [1,4],
    [2,3],
    [2,4],
    [3,4]
]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 递归, f(n,k) = f(n-1, k-1) + f(n-1, k)
        # 最后一个数字是n & 最后一个数字不是n
        if n == k: return [[_ for _ in range(1, n+1)]]
        if k == 0: return [[]]
        res1 = self.combine(n-1, k-1)
        if res1:
            res1 = [res + [n] for res in res1]
        res2 = self.combine(n-1, k)
        return res1 + res2