'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
'''

'''
Remark: use a hashtable to save target-nums[i]. Hashtable search time is O(1).
'''
# Version 1:


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res_dict = {}
        for i in range(len(nums)):
            if nums[i] in res_dict.keys():
                return (res_dict[nums[i]], i)
            else:
                res_dict[(target - nums[i])] = i


# Version 2:

class Solution(object):
    '''
    1. The use of "enumerate" in Python
    2. Omit "else"
    '''

    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num] + 1, i + 1
            d[num] = i


# Tests:
aa = Solution()
bb = print(aa.twoSum([1, 2, 7, 9], 10))
