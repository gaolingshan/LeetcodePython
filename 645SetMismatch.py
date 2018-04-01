'''
645. Set Mismatch
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

'''

# Version 1: mathematical
'''
Assuming the repeated number is a and the missing number is b.
a - b = sum(nums) - sum(range(1, len(nums)+1)) 

a + b = (a**2 - b**2) / (a - b) = (sum([i ** 2 for i in nums]) - (N * (N + 1) * (2N + 1)) / 6) / (a - b)

# sum of first N squares: (N * (N + 1) * (2N + 1)) / 6

'''
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        a_minus_b = sum(nums) - N * (N + 1) / 2
        a_plus_b = (sum([i**2 for i in nums]) - N * (N+1) * (2*N+1)/6)/ \
                   a_minus_b

        return [int((a_minus_b+a_plus_b)/2), int((a_plus_b-a_minus_b)/2)]


# Version 2: hashtable
'''
2 passes:
1. 1st pass: store the nums list in a dictionary, with count as its value.
2. 2nd pass: check the count of each value in the dictionary
'''
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            if num in d:
                a = num
            else:
                d[num] = 1
        for num in range(1, len(nums)+1):
            if d.get(num, 0) == 0:
                b = num
        return [a, b]

aa = Solution()
print(aa.findErrorNums([1,2,2,4]))


