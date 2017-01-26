'''
67. Add Binary
Difficulty: Easy
Given two binary strings, return their sum (also a binary string).
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
'''
Remark:
    参考066 Plus One, 关于加法进位的思路
'''


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pa = len(a) - 1
        pb = len(b) - 1
        temp = 0
        res = ''
        while pa > 0 and pb > 0:
            if a[pa] == '1' and b[pb] == '1':
                if temp == 1:
                    res = '1' + res
                else:
                    temp = 1
                    res = '0' + res
            elif a[pa] == '0' and b[pb] == '0':
                if temp == 1:
                    temp = 0
                    res = '1' + res
                else:
                    res = '0' + res
            else:
                if temp == 1:
                    res = '0' + res
                else:
                    res = '1' + res
            pa -= 1
            pb -= 1
        return res

A = Solution()
b = a.addBinary('11', '1')
print(b)
b = a.addBinary('111', '11')
print(b)
b = a.addBinary('10', '01')
print(B)

# https://discuss.leetcode.com/topic/12116/simple-python-solution-76ms/2
# https://discuss.leetcode.com/topic/6207/an-accepted-concise-python-recursive-solution-10-lines
# One-liner cheat: bin(int(a,2) + int(b,2))[2:]
