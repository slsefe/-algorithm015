"""547 朋友圈 中等
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1：
输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。

示例 2：
输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
 
提示：
1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friend-circles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 1. DFS, BFS, 类似岛屿问题，O(N^2)
        if not M: return 0
        visited = [False] * len(M)
        res = 0
        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, visited, i)
                res += 1
        return res

    def dfs(self, m, visited, i):
        for j in range(len(m)):
            if not visited[j] and m[i][j] == 1:
                visited[j] = True
                self.dfs(m, visited, j)

    def findCircleNum_2(self, M: List[List[int]]) -> int:
        # 2. 并查集
        if not M: return 0
        # init disjoint set
        n = len(M)
        p = [i for i in range(n)]
        # union elements
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        # cal count
        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root