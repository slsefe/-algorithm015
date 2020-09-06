"""
leetcode 264 丑数II
找出第n个丑数
丑数就是质因数只包含2，3，5的正整数
1是丑数
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 从小到大迭代，（1）找出下一个最小的丑数（2）去重
        min_heap = [1]
        seen = {1, }
        for i in range(n - 1):
            val = heapq.heappop(min_heap)
            for i in (2, 3, 5):
                if i * val not in seen:
                    heapq.heappush(min_heap, i * val)
                    seen.add(i * val)
        return heapq.heappop(min_heap)
