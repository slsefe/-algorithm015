"""leetcode 56 合并区间 中等
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对区间按照左边界排序，O(nlogn)
        intervals.sort(key=lambda x: x[0])
        # 遍历区间，合并区间，O(n)。
        merged = []
        for interval in intervals:
            # 如果当前区间的左边界大于前一个区间的右边界，则不能合并
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            # 否则，更新前一个区间的右边界
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
