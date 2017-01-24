'''
26. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

'''
Remark:

index从高到低删除，用del别用pop，or else it will only make a copy of the list and replace the numbers after
'''


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            idx = len(nums) - 1
            for i in range(len(nums) - 1, 0, -1):
                if nums[idx] == nums[idx - 1]:
                    del(nums[idx])
                idx -= 1
        # return len(nums)

a = Solution()
b = a.removeDuplicates([1, 2, 3])
print(b)
b = a.removeDuplicates([1, 1, 3])
print(b)
b = a.removeDuplicates([])
print(b)
