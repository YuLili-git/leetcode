#给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
#示例 1:
#输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
#输出: 16 
#解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
#示例 2:
#输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
#输出: 4 
#解释: 这两个单词为 "ab", "cd"。
#示例 3:
#输入: words = ["a","aa","aaa","aaaa"]
#输出: 0 
#解释: 不存在这样的两个单词。
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask_map, ans = {}, 0
        for i in range(len(words)):
            bitmask = 0
            for c in words[i]:
                bitmask |= 1 << (ord(c) - ord('a'))
            if bitmask in bitmask_map:
                bitmask_map[bitmask] = max(bitmask_map[bitmask], len(words[i]))
            else:
                bitmask_map[bitmask] = len(words[i])

        for x in bitmask_map:
            for y in bitmask_map:
                if (x & y) == 0:
                    ans = max(ans, bitmask_map[x] * bitmask_map[y])

        return ans
