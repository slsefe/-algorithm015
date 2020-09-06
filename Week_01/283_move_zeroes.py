"""
leetcode 283 移动零
给定一个数组nums，将所有0移动到数组的末尾，保持非零元素的相对顺序
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 pointers, O(n)
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1