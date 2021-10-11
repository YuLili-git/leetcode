#给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#示例 1：
#输入：nums = [2,2,3,2]
#输出：3
#示例 2：
#输入：nums = [0,1,0,1,0,1,100]
#输出：100
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i, j in dic.items():
            if j == 1:
                return i
