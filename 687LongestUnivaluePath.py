'''
687. Longest Univalue Path

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(left)
        right = self.dfs(right)

        left = left + 1 if root.left and root.left.val == root.val else 0;
        right = right + 1 if root.right and root.right.val == root.val else 0;

        self.res = max(self.res, left+right)
        return max(left, right)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res