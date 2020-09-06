"""
leetcode 1 两数之和

"""


class Solution:

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        # 1.两重循环，O(n^2),O(1)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        # 2.哈希表，两次循环,O(n), O(n)
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        for j, num in enumerate(nums):
            if target-num in d and d[target-num] != j:
                return [j, d[target-num]]

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        # 2.哈希表，两次循环,O(n), O(n)
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]
            d[num] = i