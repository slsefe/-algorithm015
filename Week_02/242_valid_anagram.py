"""
leetcode 242 有效的字母异位词
字母异位词指的是：两个单词含有的字母的个数相等
"""


class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        # 1. 哈希表，O(n), O(n)
        # 2. 排序，O(nlogn), O(1)
        if len(s) != len(t):
            return False
        from collections import defaultdict
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        for cnt in list(d.values()):
            if cnt != 0:
                return False
        return True

    def isAnagram_2(self, s: str, t: str) -> bool:
        # 1. 哈希表，O(n), O(n)
        # 2. 排序，O(nlogn), O(1)
        return sorted(s) == sorted(t)