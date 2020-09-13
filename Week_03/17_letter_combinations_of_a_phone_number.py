"""
leetcode 17 电话号码的字母组合
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits, depth, path, d, res):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            digit = digits[depth]
            for letter in d[digit]:
                path.append(letter)
                dfs(digits, depth + 1, path, d, res)
                path.pop()

        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        dfs(digits, 0, [], d, res)
        return res
