'''
66. Plus One
Difficulty: Easy

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        power = len(digits) - 1
        for digit in digits:
            num += digit * 10 ** power
            power -= 1
        num += 1
        res = [int(i) for i in str(num)]
        return res

# Version 2 : Try string manipulation
