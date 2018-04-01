'''
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.

'''

# Version 1:
class Solution:
    def dfs(self, i, j, grid):
        grid[i][j] = 0
        self.temp += 1
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            self.dfs(i + 1, j, grid)
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            self.dfs(i, j + 1, grid)
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            self.dfs(i - 1, j, grid)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            self.dfs(i, j - 1, grid)
        return

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.temp = 0
                    self.dfs(i, j, grid)
                    res = max(res, self.temp)
        return res

# Version 2:
'''
Rather than 4 if statements, it is better to use two arrays to represent 
the changes. 
'''
class Solution:
    def dfs(self, i, j, grid):
        grid[i][j] = 0
        self.temp += 1
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            new_i = i + dx[k]
            new_j = j + dy[k]
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and \
                    grid[new_i][new_j] == 1:
                self.dfs(new_i, new_j, grid)
        return

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.temp = 0
                    self.dfs(i, j, grid)
                    res = max(res, self.temp)
        return res

