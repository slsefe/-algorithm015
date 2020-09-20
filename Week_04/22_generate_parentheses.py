"""
leetcode 22 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


class Solution:
    def generateParenthesis_1(self, n: int) -> List[str]:
        # 1. recursion, 递归生成所有括号，最后判断合法性
        res = []

        def _is_valid(s):
            stack = []
            for char in s:
                if char == '(':
                    stack.append(char)
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            return not stack

        def _generate(level, max_level, s):
            # terminator
            if level >= max_level:
                if _is_valid(s):
                    res.append(s)
                return
            # process
            s1 = s + '('
            s2 = s + ')'
            # drill down
            _generate(level + 1, max_level, s1)
            _generate(level + 1, max_level, s2)
            # reverse states

        _generate(0, 2 * n, "")
        return res

    def generateParenthesis_2(self, n: int) -> List[str]:
        # 2.recursion, 在递归过程中进行剪枝
        res = []

        def _generate(left, right, n, s):
            # terminator
            if left == n and right == n:
                res.append(s)
                return
            # process
            # drill down
            if left < n:
                _generate(left + 1, right, n, s + '(')
            if left > right:
                _generate(left, right + 1, n, s + ')')
            # reverse status

        _generate(0, 0, n, "")
        return res

    def generateParenthesis_3(self, n: int) -> List[str]:
        # 3. backtracking
        res = []

        def _is_valid(s):
            stack = []
            for char in s:
                if char == '(':
                    stack.append(char)
                else:
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            return not stack

        def _generate(s):
            # terminator
            if len(s) == 2 * n:
                if _is_valid(s):
                    res.append("".join(s))
                return
            # process
            # drill down
            # reverse states
            s.append('(')
            generate(s)
            s.pop()
            s.append(')')
            generate(s)
            s.pop()

        _generate([])
        return res
