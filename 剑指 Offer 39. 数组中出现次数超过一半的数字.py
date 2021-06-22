#数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#示例 1:
#输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
#输出: 2

#############################solution 1：#############################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        dic_order=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return dic_order[0][0]

#############################solution 2：#############################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sort_num = sorted(nums)
        return sort_num[len(sort_num) // 2]
      
#############################solution 3：#############################
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        count = 0
        for i in nums:
            if vote == 0:
                x = i
            if x == i:
                vote += 1
            else:
                vote += -1
        for i in nums:
            if x == i:
                count += 1
        if count > len(nums) // 2:
            return x
            
