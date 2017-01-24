'''
20. Valid Parenthese
Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
Remark:
Use stack

'''


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in dic.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or dic[stack[-1]] == char:
                    return False
                else:
                    stack.pop()
        return stack == []

a = Solution()
b = a.isValid('{}()')
print(b)
b = a.isValid('{()}')
print(b)
b = a.isValid('(')
print(b)
b = a.isValid('()')
print(b)
b = a.isValid(']')
print(b)
b = a.isValid('([)')
print(b)
