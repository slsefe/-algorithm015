"""leetcode 322 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2
 
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. 暴力递归，O(2^N)
        # 2. BFS，转换为求值为0的结点的最小层数
        # 3. DP，O(N), O(N)
        # a 分治：f(amount) = 1 + min(f(amount-coins[i]) for i in range(len(coins)))
        # b 定义状态数组：dp[i]表示金额为i时的最少硬币数量，-1表示不存在
        # c DP方程：dp[i] = 1 + min(f(i-coin) for coin in coins)
        dp = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            amount_list = []
            for coin in coins:
                if i-coin >= 0 and dp[i-coin] != -1:
                    amount_list.append(i-coin)
            if amount_list:
                dp[i] = 1 + min(dp[j] for j in amount_list)
            else:
                dp[i] = -1
        return dp[-1]
