#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。
#示例 1：
#输入：nums = [-1,0,1,2,-1,-4]
#输出：[[-1,-1,2],[-1,0,1]]
#示例 2：
#输入：nums = []
#输出：[]
#示例 3：
#输入：nums = [0]
#输出：[]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right:
                        left += 1
                        if nums[left] != nums[left - 1]:
                            break
                    while left < right:
                        right -= 1
                        if nums[right] != nums[right + 1]:
                            break
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res
