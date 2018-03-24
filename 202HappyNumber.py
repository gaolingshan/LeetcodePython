'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
'''

'''
Create an empty set to save the sums.
Let's implement the iteration.
Calculate sum of square of the integers.
As long as the result is not 1, check:
if it can be found in the set, which means that it has run into a cycle. 
In this case, it is not a happy number. 
or else just add the sum to the set.

Set access O(1)
'''

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_set = set()
        while n != 1:
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n in sum_set:
                return False
            else:
                sum_set.add(n)
        return True


aa = Solution()
print(aa.isHappy(20))

