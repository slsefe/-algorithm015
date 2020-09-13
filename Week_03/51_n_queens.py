"""
leetcode 51 N皇后
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []
        self.res = []
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n, 0, [])
        return self._gen_res(n)

    def dfs(self, n, row, cur_state):
        # 1. recursion terminator
        if row >= n:
            self.res.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            # 3. drill down
            self.dfs(n, row + 1, cur_state + [col])
            # 4. reverse status
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _gen_res(self, n):
        boards = []
        for cols in self.res:
            board = []
            for col in cols:
                board.append("." * col + "Q" + "." * (n - col - 1))
            boards.append(board)
        return boards
