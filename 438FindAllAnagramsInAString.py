'''
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

'''
Tags: two pointers, hashtable

Thoughts:
Maintain a dictionary and a sliding window. Each element is visited twice. Time 
complexity = O(n)

Steps:
Save p as a Counter(p).
Now check the sliding window with left pointer 'l' and right pointer 'r'.
For each element that 'r' is pointer to, deduct one value from Counter(p). 
For a valid window, all values in counters should be zero and len(window) == 
len(p).
If value become negative, then move 'l', until 'l' > 'r'.

'''
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        d = Counter(p)
        len_p = len(p)
        l = r = 0
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) - 1
            while l <= r and d[s[r]] < 0:
                d[s[l]] += 1
                l += 1
            if r - l + 1 == len_p:
                res.append(l)
            r += 1
        return res


aa = Solution()
print(aa.findAnagrams("abab", "ab"))
