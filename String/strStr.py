#coding:utf-8

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        elif needle.strip() == '':
            return 0
        # elif haystack == needle:
        #     return 0
        else:
            index = 0
            nlen =len(needle)
            hlen = len(haystack)
            for i in range(hlen):
                if haystack[i] == needle[0]:
                    index = i
                    break
            else:
                return -1
            while(index + nlen <= hlen):
                # 切片，取前不取后所以需要超出一个
                if haystack[index:index + nlen] == needle:
                    return index
                else:
                    index += 1
            return -1



haystack = "a"

needle = "a"
print  Solution().strStr(haystack,needle)