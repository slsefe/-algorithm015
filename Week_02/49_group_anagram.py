"""
leetcode 49 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
所有输入均为小写字母。
不考虑答案输出的顺序。
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 排序，哈希表，O(NKlogK),N为字符串个数，K为字符串最大长度
        # 每个str排序，为key，排序前为value
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())