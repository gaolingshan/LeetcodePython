'''
58. Length of Last Word
Difficulty: Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                if count != 0:
                    break
        return count

# Try two pointers

a = Solution()
b = a.lengthOfLastWord('Hello World')
print(b)
b = a.lengthOfLastWord(' ')
print(b)
b = a.lengthOfLastWord('abc cd')
print(b)
b = a.lengthOfLastWord('dnfakl ')
print(b)
b = a.lengthOfLastWord('d')
print(b)
