"""leetcode 70 爬楼梯（easy）
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def climbStairs_1(self, n: int) -> int:
        # 1. 递归，O(2^n), O(n)
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs_2(self, n: int) -> int:
        # 2. 带缓存的递归，O(n), O(n)
        def _helper(n, res):
            if n == 1: return 1
            if n == 2: return 2
            if res[n] == 0:
                res[n] = _helper(n-1, res) + _helper(n-2, res)
            return res[n]

        res = [0] * (n+1)
        return _helper(n, res)

    def climbStairs_3(self, n: int) -> int:
        # 3. 递推迭代，O(n), O(n)
        res = [0, 1, 2]
        for i in range(3, n+1):
            res.append(res[-2] + res[-1])
        return res[n]

    def climbStairs_4(self, n: int) -> int:
        # 4. 优化的递推迭代，O（n）， O（1）
        if n == 1: return 1
        if n == 2: return 2
        p, q = 1, 2
        for i in range(3, n+1):
            p, q = q, p+q
        return q

