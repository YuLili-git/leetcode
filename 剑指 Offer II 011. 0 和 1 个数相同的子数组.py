#给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#示例 1:
#输入: nums = [0,1]
#输出: 2
#说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
#示例 2:
#输入: nums = [0,1,0]
#输出: 2
#说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        ret = tmp = 0
        for index, num in enumerate(nums):
            if num == 0:
                tmp += -1
            else:
                tmp += 1
            if tmp in dic:
                ret = max(ret, index - dic[tmp])
            else:
                dic[tmp] = index
        return ret
