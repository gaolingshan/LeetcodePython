'''
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''

'''
Note: Bit-wise (num & 1) is equivalent to (num % 2)
similarly, (num & 2) is equivalent to check if the second to last digit is '2'...
'''


'''
Thoughts:
The longest result include all the characters that have shown up for even times
+ the characters show up (odd - 1) times
+ the one character in the center, if these are any odd numbers at all.

equivalent to
length of all characters - total number of odd numbers
if any odd numbers at all, res + 1
'''

from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_d = Counter(s)
        odd_count = 0
        for k, v in s_d.items():
            odd_count += v % 2
        return len(s) - odd_count + (odd_count > 0)
