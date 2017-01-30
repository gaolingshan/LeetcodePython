'''
118. Pascal's Triangle
Difficulty: Easy

Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

'''
Remark: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0
 +  0 1 3 3 1
 =  1 4 6 4 1
'''


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows = 1:
            return [[1]]
        else:
            for i in range(1, numRows):
                ls.append[0]
                ls =
                for res
