#请实现一个函数，把字符串 s 中的每个空格替换成"%20"
class Solution:
    def replaceSpace(self, s: str) -> str:
        new_str=s.replace(" ","%20")
        return new_str
