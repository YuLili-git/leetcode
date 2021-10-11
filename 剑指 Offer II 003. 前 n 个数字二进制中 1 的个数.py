#给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。
#示例 1:
#输入: n = 2
#输出: [0,1,1]
#解释: 
#0 --> 0
#1 --> 1
#2 --> 10
#示例 2:
#输入: n = 5
#输出: [0,1,1,2,1,2]
#解释:
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#5 --> 101
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(x):
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones

        bits = [count_ones(i) for i in range(n + 1)]
        #bits = []
        #for i in range(n + 1):
        #    bits.append(count_ones(i))
        return bits
