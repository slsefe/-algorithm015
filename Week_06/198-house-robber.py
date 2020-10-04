"""leetcode 198 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def rob_1(self, nums: List[int]) -> int:
        # DP, O(n)，分治的另一种思路
        # 1. 分治：f(n) = max(f(n-2), f(n-3)) + nums[n]
        # 2. 状态数组：dp[i]表示偷窃i号及之前房屋可以得到的最高金额
        # 3. DP方程：dp[i] = max(dp[i-3], dp[i-2]) + nums[i]
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        dp = nums[:]
        dp[2] += dp[0]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-3], dp[i-2]) + nums[i]
        return max(dp)

    def rob_2(self, nums: List[int]) -> int:
        # DP, O(n), O(n)
        # 1. 分治：f(n) = max(f(n-1), f(n-2)+nums[n])
        # 2. 状态数组：dp[i]截至目前房屋可以获得的最高金额
        # 3. DP方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        dp = nums[:]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    def rob_3(self, nums: List[int]) -> int:
        # DP, O(n), O(1)，只保留前两个状态
        # 1. 分治：f(n) = max(f(n-1), f(n-2)+nums[n])
        # 2. 状态数组：dp[i]截至目前房屋可以获得的最高金额
        # 3. DP方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        pre, now = 0, 0
        for num in nums:
            pre, now = now, max(pre+num, now)
        return now
