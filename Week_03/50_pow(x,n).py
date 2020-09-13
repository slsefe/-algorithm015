"""
leetcode 50 pow(x,n)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n%2 == 1:
                return helper(x*x, n//2) * x
            else:
                return helper(x*x, n//2)
        if x == 0: return 0
        if n < 0:
            x = 1/x
            n = -n
        return helper(x, n)