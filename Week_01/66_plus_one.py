"""
leetcode 66 加一
"""


class Solution:
    def plusOne_1(self, digits: List[int]) -> List[int]:
        # 1. 遍历数组，构造整数，加一，构造数组，O(n)，O(n)
        num = 0
        for i in digits:
            num = 10*num + i
        num += 1
        res = []
        while num > 0:
            res.append(num%10)
            num = num//10
        return res[::-1]

    def plusOne_2(self, digits: List[int]) -> List[int]:
        # 2. 倒序遍历数组，加一，进位，O(n), O(n)
        for i in range(len(digits)-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                return digits
        return [1]+digits