'''
38. Count and Say
Difficulty: Easy 
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            seq = '1'
            while n > 1:
                res = ''
                count = 1
                for i in range(1, len(seq)):
                    if seq[i] == seq[i - 1]:
                        count += 1
                    else:
                        res += str(count) + seq[i - 1]
                        count = 1
                # This is how to handle the last letter
                res += str(count) + seq[-1]
                seq = res
                n -= 1
            return seq

a = Solution()
b = a.countAndSay(1)
print(b)
b = a.countAndSay(2)
print(b)
b = a.countAndSay(3)
print(b)
b = a.countAndSay(4)
print(b)
