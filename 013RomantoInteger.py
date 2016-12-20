'''
13. Roman to Integer
Difficulty: Easy
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

'''
Remark:
Compare to 12. Integer to Roman
Roman numerals:
I : 1
V : 5
X : 10
L : 50
C : 100
D : 500
M : 1000
'''

# Version 1


class Solution(object):
    '''
    if letter i is greater than letter i + 1, then -= letter; else, += letter
    '''

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 >= len(s):
                res += roman_dic[s[i]]
            elif roman_dic[s[i]] < roman_dic[s[i + 1]]:
                res -= roman_dic[s[i]]
            else:
                res += roman_dic[s[i]]
        return res

# Tests:
aa = Solution()
print(aa.romanToInt('I'))
print(aa.romanToInt('IV'))
print(aa.romanToInt('LXX'))
print(aa.romanToInt('MMMCMXCIX'))
