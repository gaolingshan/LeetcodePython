'''
28. Implement strStr()
Difficulty: Easy

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        for i in range(len(haystack) - nlen + 1):
            if haystack[i: i + nlen] == needle:
                return i
        return -1
