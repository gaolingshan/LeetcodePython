'''
20. Valid Parentheses
Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
Tag: string, stack, hashtable

Thoughts: for each character in string, 
if it is the first half of the  parentheses, append to list; 
elif it is the second half, check if len(list) is 0, or list[-1] is not its 
counterpart, then it is false;
else pop the stack.

if the final stack is empty (NOTE: use len(stack) == 0 rather than stack == [
]. the former is faster), then the string is valid.

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
        return len(stack) == 0



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
