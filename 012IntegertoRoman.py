'''
12. Integer to Roman
Difficulty:Medium

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

'''
Remark:
Compare with the question "Roman to Integer"
'''


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        i = 0
        ls = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for j in range(len(str(num))):
            last_digit = num % 10
            if last_digit <= 3 and last_digit >= 0:
                tmp = ls[i] * last_digit
            elif last_digit == 4:
                tmp = ls[i] + ls[i + 1]
            elif last_digit == 5:
                tmp = ls[i + 1]
            elif last_digit <= 8 and last_digit >= 6:
                tmp = ls[i + 1] + ls[i] * (last_digit - 5)
            elif last_digit == 9:
                tmp = ls[i] + ls[i + 2]
            res = tmp + res
            num = (num - last_digit) // 10
            i += 2
        return res

# Tests:
aa = Solution()
print(aa.intToRoman(6))
print(aa.intToRoman(13))
print(aa.intToRoman(1))
print(aa.intToRoman(3999))
print(aa.intToRoman(7))
