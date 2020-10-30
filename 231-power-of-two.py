"""leetcode 231 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 20 = 1

示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPowerOfTwo_1(self, n: int) -> bool:
        # 2的幂次只有一个1，非2的幂次有超过1个1
        # n & (n-1)将最低位的1置0，若置0之后等于0，说明为2的幂次
        return n != 0 and (n & (n-1) == 0)

    def isPowerOfTwo_2(self, n: int) -> bool:
        # 2的幂次只有一个1，非2的幂次有超过1个1
        # n & (-n)只保留最低位的1，若等于自身，说明为2的幂次
        return n != 0 and (n & (-n) == n)