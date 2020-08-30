"""leetcode 42 接雨水

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height + [0]
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                j = stack.pop()
                if not stack: break
                res += (min(height[stack[-1]], height[i]) - height[j]) * (i - stack[-1] - 1)
            stack.append(i)
        return res
