"""
leetcode 189 旋转数组
给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数
"""


class Solution:
    def rotate_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 旋转k次，O(kn)
        k = k % len(nums)
        for i in range(k):
            last = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = last

    def rotate_2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2. 全局&部分反转，O(n)
        k = k % len(nums)

        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
