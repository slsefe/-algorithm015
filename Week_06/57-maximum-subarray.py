"""leetcode 57 最大子数组和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSubArray_1(self, nums: List[int]) -> int:
        # 1. 暴力两重遍历，O(n^2), O(1)
        res = -2147483648
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, sum(nums[i: j+1]))
        return res

    def maxSubArray_2(self, nums: List[int]) -> int:
        # 2. DP, O(n), O(n)
        # a. 分治（子问题）：从后往前，包含第n个元素的最大和由包含第n-1个元素的最大和决定,
        # max_sum(i) = max(max_sum(i-1), 0) + nums[i]
        # b. 定义状态数组：一维数组dp[i]，表示包含第i个元素的子序列最大和
        # c. DP方程：dp[i] = max(dp[i-1], 0) + nums[i]
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)

    def maxSubArray_3(self, nums: List[int]) -> int:
        # 3. DP, O(n), O(1)
        dp = nums[0]
        max_sum = dp
        for i in range(1, len(nums)):
            dp = max(dp, 0) + nums[i]
            max_sum = max(max_sum, dp)
        return max_sum


