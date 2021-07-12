#统计一个数字在排序数组中出现的次数。
#示例 1:
#输入: nums = [5,7,7,8,8,10], target = 8
#输出: 2
#示例 2:
#输入: nums = [5,7,7,8,8,10], target = 6
#输出: 0
##############################solution 1##############################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i == target:
                count += 1
        return count

##############################solution 2##############################      
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j :
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        if j >= 0 and nums[j] != target:
            return 0
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1
