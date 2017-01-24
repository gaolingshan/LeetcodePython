'''
36. Valid Sudoku
Difficulty: Easy

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

'''
Solutions:
https://discuss.leetcode.com/topic/20016/1-7-lines-python-4-solutions/3
'''

# Version 1:
# Use three groups of tuples


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        filled = []
        num_set = {'.', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char not in num_set:
                    return False
                elif char != '.':
                    filled += [(i, char), (c, char), (i // 3, j // 3, char)]

        return len(filled) == len(set(filled))

# Version 2:
# Use three 9*9 matrix of true/false as flags
