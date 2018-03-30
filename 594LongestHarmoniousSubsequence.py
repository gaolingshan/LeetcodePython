'''

594. Longest Harmonious Subsequence

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

'''
'''
from collections import defaultdict

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        for j in (-1, 1):
            if d[num + j] != 0:
                res = max(d[num + j] + d[num], res)
        return res
'''

class Solution(object):

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Save array as a Counter
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        res = 0

        for k in d:
            if (k + 1) in d:
                res = max(d[k + 1] + d[k], res)
        return res


aa = Solution()
#print(aa.findLHS([1,3,2,2,5,2,3,7]))
print(aa.findLHS([1,1,1,1]))