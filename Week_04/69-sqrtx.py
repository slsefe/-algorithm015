"""
leetcode 69 x的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def mySqrt_1(self, x: int) -> int:
        # 1. binary search
        # y=x^2在(x>0)时单调自增，x存在下界0和上界y，所以可以使用二分查找
        # 结果res是满足res^2<=x的最大整数
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def mySqrt_2(self, x: int) -> int:
        # 2. 牛顿迭代法
        # 需要推导f(x) = x^2 + a, f'(x) = 2x
        # f(x) = f(x0) + (x-x0) * f'(x0)
        # let f(x) = 0, then x = (x0 + a/x0) / 2
        r = x
        while r * r > x:
            r = int((r + x / r) / 2)
        return r

