"""leetcode 212 单词搜索II 困难
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create Trie using words
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        # backtrack
        row_cnt = len(board)
        col_cnt = len(board[0])
        matched_words = []

        def backtracking(row: int, col: int, parent: dict):
            letter = board[row][col]
            cur_node = parent[letter]
            word_match = cur_node.pop(WORD_KEY, False)
            if word_match:
                matched_words.append(word_match)
            board[row][col] = '#'
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < row_cnt and 0 <= new_col < col_cnt and board[new_row][new_col] in cur_node:
                    backtracking(new_row, new_col, cur_node)
                else:
                    continue
            board[row][col] = letter

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return matched_words
