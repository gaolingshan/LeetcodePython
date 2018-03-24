'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

'''

'''
Tag: Hashtable

Similar: 290 Word Pattern
'''



# Version 1: Original
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = True
            if (s[i] in d_s) and (t[i] in d_t):
                if (d_s[s[i]] != t[i]) or (d_t[t[i]] != s[i]):
                    flag = False
            elif (s[i] not in d_s) and (t[i] not in d_t):
                d_s[s[i]] = t[i]
                d_t[t[i]] = s[i]
            else:
                flag = False
        return flag

# Version 2: One-liner with set but slow

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))



'''
Thought Process:
To check pattern, need to create two dictionaries to store the information for both strings.
1. Check the last position they (the two elements) showed up. If different, then return false.
2. If same, then update the current position as the index value that they show up.
'''

# Version 3
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d_s, d_t = {}, {}
        for i in range(len(s)):
            if d_s.get(s[i]) != d_t.get(t[i]):
                return False
            d_s[s[i]] = i
            d_t[t[i]] = i
        return True



# Test case:
s,t  = "egg", "add"
aa = Solution()
print(aa.isIsomorphic(s, t))

s,t  = "abc", "add"
aa = Solution()
print(aa.isIsomorphic(s, t))