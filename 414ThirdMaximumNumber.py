'''
414. Third Maximum Number
Difficulty: Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [float('-inf'), float('-inf'), float('-inf')]
        for number in nums:
            if number not in res:
                if number > res[0]:
                    res = [number, res[0], res[1]]
                elif number > res[1]:
                    res = [res[0], number, res[1]]
                elif number > res[2]:
                    res = [res[0], res[1], number]
        return max(res) if float('-inf') in res else res[2]
