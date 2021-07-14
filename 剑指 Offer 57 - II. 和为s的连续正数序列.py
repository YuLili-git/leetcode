#输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#示例 1：
#输入：target = 9
#输出：[[2,3,4],[4,5]]
#示例 2：
#输入：target = 15
#输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#限制：
#1 <= target <= 10^5
#################################solution 1 #################################
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1
        j = 2
        res = []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i *i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res
#################################solution 2 #################################
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1
        j = 2
        s = 3
        res = []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            if s < target:
                j += 1
                s += j
        return res
