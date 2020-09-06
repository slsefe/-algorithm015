"""
leetcode 347 前k个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 哈希表+小顶堆
        # step1, 统计次数
        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        # step2, min heap
        d = list(d.items())
        min_heap = []
        for item in d[:k]:
            heapq.heappush(min_heap, (item[1], item[0]))
        for item in d[k:]:
            if item[1] > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (item[1], item[0]))
        return [x[1] for x in min_heap]
