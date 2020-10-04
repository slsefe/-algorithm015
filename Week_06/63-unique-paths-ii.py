"""leetcode 63 不同路径II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP, O(m*n), O(m*n)
        if obstacleGrid[0][0] == 1: return 0  # 不用多余计算
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n] * m
        for i in range(m):
            for j in range(n):
                # 障碍物的路径为0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:  # 起始点如果不是障碍物，路径为1，只有m=n=1时会用到
                        dp[i][j] = 1
                    elif i == 0:  # 第一行不再全为1，根据障碍物矩阵和前一个格子计算
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:  # 第一列不再全为1，根据障碍物矩阵和上一个格子计算
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]  # 普通情况，递推公式
        return dp[m-1][n-1]

    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        # 2. DP, O(m*n), O(n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [-1] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[j] = 1
                    elif i == 0:
                        dp[j] = dp[j-1]
                    elif j == 0:
                        dp[j] = dp[j]
                    else:
                        dp[j] += dp[j-1]
        return dp[-1]
