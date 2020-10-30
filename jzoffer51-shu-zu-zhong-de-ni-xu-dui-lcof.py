"""剑指offer 51 数组中的逆序对 困难
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
 
限制：0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, start, end):
        # terminator
        if start >= end:
            return 0
        # split and sort
        mid = (start + end) >> 1
        count = self.merge_sort(nums, start, mid) + self.merge_sort(nums, mid + 1, end)
        # merge and counting
        temp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
                count += (j - (mid + 1))
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
            count += (j - (mid + 1))
        while j <= end:
            temp.append(nums[j])
            j += 1
        # copy
        nums[start: end + 1] = temp[:]
        return count
