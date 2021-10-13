#给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#变位词 指字母相同，但排列不同的字符串。
#示例 1:
#输入: s = "cbaebabacd", p = "abc"
#输出: [0,6]
#解释:
#起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
#起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。
# 示例 2:
#输入: s = "abab", p = "ab"
#输出: [0,1,2]
#解释:
#起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
#起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
#起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr1, arr2, n, res = [0] *26, [0] * 26, len(p), []
        if n > len(s):
            return []
        for i in range(n):
            arr1[ord(p[i]) - ord('a')] += 1
            arr2[ord(s[i]) - ord('a')] += 1
        if arr1 == arr2:
            res.append(0)
        for i in range(n, len(s)):
            arr2[ord(s[i]) - ord('a')] += 1
            arr2[ord(s[i - n]) - ord('a')] -= 1
            if arr1 == arr2:
                res.append(i - n + 1)
        return res
