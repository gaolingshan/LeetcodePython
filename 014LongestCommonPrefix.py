'''
14. Longest Common Prefix
Difficulty:Easy
Write a function to find the longest common prefix string amongst an array of strings.
'''

# Version 1: O(n*m), n is number of strings in the array, m is length of
# the shortest string


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == []:
            return ''

        m = len(strs[0])
        tmp = strs[0]
        res = ''
        for string in strs:
            if len(string) < m:
                m = len(string)
                tmp = string

        i = 0
        flag = False
        while i < len(tmp):
            for string in strs:
                if tmp[i] != string[i]:
                    res = tmp[0:i]
                    flag = True
                    break
                else:
                    res = tmp[0:(i + 1)]
            if flag:
                break
            i += 1
        return res


# Version2: use "reduce" function

class Solution:

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]

    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp, strs)

# Tests:
aa = Solution()
print(aa.longestCommonPrefix(['aa', 'ab']))
print(aa.longestCommonPrefix(['aa', 'aa']))
print(aa.longestCommonPrefix(['aa', 'bb', 'cc']))
print(aa.longestCommonPrefix(['stu', 'st', 's']))
