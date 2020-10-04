"""leetcode 120 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minimumTotal_1(self, triangle: List[List[int]]) -> int:
        # 1. 暴力，枚举所有情况，n层，left or right：2^N
        # 2. 递归, O(n^2), O(n^2)
        # f(i, j) = triangle[i][j] + min(f(i+1, j), f(i+1, j+1))
        def helper(i, j, triangle):
            if i == len(triangle) - 1:
                return triangle[i][j]
            left = helper(i + 1, j, triangle)
            right = helper(i + 1, j + 1, triangle)
            return min(left, right) + triangle[i][j]
        return helper(0, 0, triangle)

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        # 3. DP, top-down iteration, O(n^2), O(n^2)
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(res)):
            for j in range(len(res[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(res[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])

    def minimumTotal_3(self, triangle: List[List[int]]) -> int:
        # 4. DP, bottom-up, O(n^2), O(n^2)
        # a. 找重复性，进行分治 solution(i,j) = a[i][j] + min(sub(i+1, j), sub(i+1, j+1))
        # b. 定义状态数组: dp[i, j]
        # c. DP方程: dp[i][j] = a[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        dp = triangle  # trickly part
        for i in range(len(dp)-2, -1, -1):  # 从倒数第二层开始
            for j in range(len(dp[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]

    def minimumTotal_4(self, triangle: List[List[int]]) -> int:
        # 5. DP, bottom-up, O(n^2), O(n)
        # dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
