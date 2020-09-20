"""
leetcode 126 单词接龙II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 边界条件
        res = []
        word_set = set(wordList)
        if beginWord in word_set: word_set.remove(beginWord)
        if not word_set or endWord not in word_set: return res
        # BFS得到后继节点列表
        successors = collections.defaultdict(set)
        if not self.__bfs(beginWord, endWord, word_set, successors):
            return res
        # 回溯得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = collections.deque()
        queue.append(beginWord)
        visited = set(beginWord)
        next_level_visited = set()
        found = False
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                for j in range(len(word)):
                    for k in string.ascii_lowercase:
                        next_word = word[:j] + k + word[j+1:]
                        if next_word in word_set and next_word not in visited:
                            if next_word == endWord:
                                found = True
                            if next_word not in next_level_visited:
                                next_level_visited.add(next_word)
                                queue.append(next_word)
                            successors[word].add(next_word)
            if found: break
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path.copy())
            return
        if beginWord not in successors:
            return
        for next_word in successors[beginWord]:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()
