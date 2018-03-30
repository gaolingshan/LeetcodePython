'''
20. Valid Parenthese
Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
Tag: string, stack
Thoughts:

'''


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in d.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or d[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        return stack == []



a = Solution()
b = a.isValid('{}()')
assert b
b = a.isValid('{()}')
assert b
b = a.isValid('(')
assert b == False
b = a.isValid('()')
assert b
b = a.isValid(']')
assert b == False
b = a.isValid('([)')
assert b == False
