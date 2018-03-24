'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

'''

# Version 1:
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pt={};st={}
        str=str.split()
        if len(pattern)!=len(str):return False
        for i in range(len(pattern)):
            if pt.get(pattern[i],0)!=st.get(str[i],0):
                return False
            pt[pattern[i]]=i+1
            st[str[i]]=i+1
        return True


# Version 2: Slow

'''
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        flag = False
        str_ls = str.split()
        if len(str_ls) == len(pattern):
            flag = len(set(zip(str_ls, pattern))) == len(set(str_ls)) == len(set(pattern))
        return flag
'''

aa = Solution()
print(aa.wordPattern("abba", "dog cat cat dog"))