"""
leetcode 200 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1

示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, 将相邻的1一次性变为0，dfs的次数即为岛屿数量
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, m, n, i, j)
                    res += 1
        return res

    def dfs(self, grid, m, n, x, y):
        # terminator
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
            return
        # process
        grid[x][y] = '0'
        # drill down
        self.dfs(grid, m, n, x - 1, y)
        self.dfs(grid, m, n, x + 1, y)
        self.dfs(grid, m, n, x, y - 1)
        self.dfs(grid, m, n, x, y + 1)
        # reverse states

    def numIslands_2(self, grid: List[List[str]]) -> int:
        # bfs,
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, m, n, i, j)
                    res += 1
        return res

    def bfs(self, grid, m, n, x, y):
        queue = collections.deque()
        queue.append((x, y))
        grid[x][y] = '0'  # 在入队列而不是出队列的时候进行标记，否则会有重复入队列情况
        while queue:
            x, y = queue.popleft()
            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = '0'

