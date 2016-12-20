'''
9. Palindrome Number
Difficulty:
    Easy
Determine whether an integer is a palindrome. Do this without extra space.
Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

'''
Remark: Count digit of an integer
1. len(str(integer))
2. int(log10(integer))+1
Time is about the same for both methods
'''
# Version 1: Use the same logic as reverse integers


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x > 2147483647:
            return False
        else:
            res = 0
            remain = x
            for i in range(len(str(x)) // 2):
                res = res * 10 + remain % 10
                remain = (remain - remain % 10) // 10
            if len(str(x)) % 2 == 0:
                if res == remain:
                    return True
                else:
                    return False
            elif len(str(x)) / 2 != 0:
                if res == ((remain - remain % 10) / 10):
                    return True
                else:
                    return False


# Version 2: Without reversing the integer.

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x > 2147483647:
            return False
        else:
            length = len(str(x))
            while length >= 1:
                last_digit = x % 10
                x -= last_digit * 10**(length - 1)
                x //= 10
                length -= 2
            return x == 0

# Tests:
aa = Solution()
print(aa.isPalindrome(10))
