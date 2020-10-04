"""leetcode 62 不同路径 medium
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @lru_cache
    def uniquePaths_1(self, m: int, n: int) -> int:
        # 1. 带缓存的递归，O(m+n), O(m+n)
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

    def uniquePaths_2(self, m: int, n: int) -> int:
        # 2. DP，O(m*n), O(m*n)
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1, n-1]

    def uniquePaths_3(self, m: int, n: int) -> int:
        # 3. DP, O(m*n), O(2n)
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = cur[j-1] + pre[j]
            pre = cur[:]
        return cur[-1]

    def uniquePaths_4(self, m: int, n: int) -> int:
        # 4. DP, O(m*n), O(n)
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

    def uniquePaths_5(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
