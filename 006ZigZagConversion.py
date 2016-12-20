
'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

'''
Remark:

1. Create numRows of lists, ls1, ls2, ls3...etc.
2. Loop through the given string, for each letter in the string, put them in the list they belong to.
3. Use an index counter, when the counter hit the bottom row, change direction. Until it hits the top row, then change the direction again.
4. Corner cases are when there are only numRows is 1 or numRows >= len(s).
'''

# Version 1:


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        # Pythonic syntax, create numRows of strings in a list
        res_list = [''] * numRows
        counter, step = 0, 1
        for c in s:
            res_list[counter] += c
            if counter == 0:
                step = 1
            elif counter == numRows - 1:
                step = -1
            counter += step

        return ''.join(res_list)

# tests:
aa = Solution()
print(aa.convert('test', 2))

bb = Solution()
print(bb.convert('test', 1))
