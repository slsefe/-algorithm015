"""leetcode 152 最大子数组积
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct_1(self, nums: List[int]) -> int:
        # 1. 暴力，两重循环，O(n^3), O(1)
        res = -2147483638
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = 1
                for k in range(i, j + 1):
                    prod *= nums[k]
                res = max(res, prod)
        return res

    def maxProduct_2(self, nums: List[int]) -> int:
        # 2. DP, O(n),O(n)
        # a. 分治：max_prod(i) = max(max_prod(i-1)*nums[i], min_prod(i-1)*nums[i], nums[i])
        # b. 定义状态数组:
        # max_prod[i]表示以第i个元素结尾的子数组最大乘积
        # min_prod[i]表示以第i个元素结尾的子数组最小乘积
        # c. DP方程：
        # dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        # dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        dp_max = nums[:]
        dp_min = nums[:]
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        return max(dp_max)

    def maxProduct_3(self, nums: List[int]) -> int:
        # 3. DP, O(n), O(1)
        # a. 分治：max_prod(i) = max(max_prod(i-1)*nums[i], min_prod(i-1)*nums[i], nums[i])
        # b. 定义状态数组:
        # dp_max表示以第i个元素结尾的子数组最大乘积
        # dp_min表示以第i个元素结尾的子数组最小乘积
        # c. DP方程：
        # dp_max = max(dp_max*nums[i], dp_min*nums[i], nums[i])
        # dp_min = min(dp_max*nums[i], dp_min*nums[i], nums[i])
        dp_max, dp_min = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmp_max, tmp_min = dp_max, dp_min  # dp_max和dp_min需要先存下来
            dp_max = max(tmp_max*nums[i], tmp_min*nums[i], nums[i])
            dp_min = min(tmp_max*nums[i], tmp_min*nums[i], nums[i])
            res = max(res, dp_max)
        return res
