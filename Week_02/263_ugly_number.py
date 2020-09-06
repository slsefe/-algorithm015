"""
leetcode 263 丑数
判断给定的数是否为丑数
丑数就是质因数只包含2，3，5的正整数
1是丑数
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1: return False
        if num == 1: return True
        if num % 2 == 0: return self.isUgly(num // 2)
        if num % 3 == 0: return self.isUgly(num // 3)
        if num % 5 == 0: return self.isUgly(num // 5)
        return False
