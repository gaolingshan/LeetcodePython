'''
387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

'''
Tag: hashtable

Thoughts: two passes. 1st pass: store in a dictionary. 2nd pass: check count
'''


from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        # Without calling Counter:

        d = {}
        for i in range(len(s)):
            d[s] = d.get(s, 0) + 1        
        '''

        d = Counter(s)
        for i in range(len(s)):
            if d.get(s[i], -1) == 1:
                return i
        return -1