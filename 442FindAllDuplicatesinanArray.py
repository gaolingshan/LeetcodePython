'''
442. Find All Duplicates in an Array
Difficulty: Medium
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

'''
Remark: refer to 448 and apply similar logic.
'''


class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if nums[ind] < 0:
                res.append(ind + 1)
            else:
                nums[ind] = nums[ind] * (-1)
        return res
