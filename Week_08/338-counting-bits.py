"""leetcode 338 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def countBits_1(self, num: int) -> List[int]:
        # 循环n次，每次计算一个数字的二进制表示中1的个数（leetcode 191）
        # O(n*sizeof(integer))
        res = []
        for i in range(num + 1):
            res.append(self.count(i))
        return res

    def count(self, num):
        cnt = 0
        while num != 0:
            num &= (num - 1)
            cnt += 1
        return cnt

    def countBits_2(self, num: int) -> List[int]:
        # f(i + b) = f(i) + 1, for b = 2^m and b > i
        # DP, O(n)
        res = [0] * (num + 1)
        i = 0
        b = 1
        while b <= num:
            # calculate [b, 2b) or [b, num)
            while i < b and b + i <= num:
                res[b + i] = res[i] + 1
                i += 1
            i = 0
            b <<= 1
        return res

    def countBits_3(self, num: int) -> List[int]:
        # f(n) = f(n/2) + n mod(2)
        # DP, O(n)
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + i % 2
        return res

    def countBits_4(self, num: int) -> List[int]:
        # f(n) = f(n&(n-1)) + 1
        # DP, O(n)
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i & (i - 1)] + 1
        return res
