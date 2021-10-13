#给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。
#换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
#示例 1：
#输入: s1 = "ab" s2 = "eidbaooo"
#输出: True
#解释: s2 包含 s1 的排列之一 ("ba").
#示例 2：
#输入: s1= "ab" s2 = "eidboaoo"
#输出: False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2, lg = [0] * 26, [0] * 26, len(s1)
        if lg > len(s2):
            return False
        for i in range(lg):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        for i in range(lg, len(s2)):
            if arr1 == arr2:
                return True
            arr2[ord(s2[i - lg]) - ord('a')] -= 1
            arr2[ord(s2[i]) - ord('a')] += 1
        return arr1 == arr2
