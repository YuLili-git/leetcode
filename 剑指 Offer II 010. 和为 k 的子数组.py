#给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。
#示例 1 :
#输入:nums = [1,1,1], k = 2
#输出: 2
#解释: 此题 [1,1] 与 [1,1] 为两种不同的情况
#示例 2 :
#输入:nums = [1,2,3], k = 3
#输出: 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = num = 0
        dic = {0:1}
        for i in nums:
            num += i
            ret += dic.get(num - k, 0)
            dic[num] = dic.get(num, 0) + 1
        return ret
