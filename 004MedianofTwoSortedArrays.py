# 4. Median of Two Sorted Arrays
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_nums = []
        length = min(len(nums1), len(nums2))
        # compare two arrays up to <length>
        while (i < length) and (j < length) and (i+j) < length//2:
                if nums1[i] < nums2[j]:
                    merged_nums.append(nums1[i])
                    i+=1
                elif nums1[i] == nums2[j]:
                    merged_nums.extend([nums1[i], nums2[j]])
                    i+=1
                    j+=1
                else:
                    merged_nums.append(nums[j])
                    j+=1
        if i == length:
            merged_nums.extend(nums1[i:])
        elif j == length:
            merged_nums.extend(nums2[j:])
        return
