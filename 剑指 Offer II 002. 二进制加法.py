#给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
#输入为 非空 字符串且只包含数字 1 和 0。
#示例 1:
#输入: a = "11", b = "10"
#输出: "101"
#示例 2:
#输入: a = "1010", b = "1011"
#输出: "10101"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x = answer
            y = carry
        return bin(x)[2:]
