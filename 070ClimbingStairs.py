'''
70. Climbing Stairs
Difficulty: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''

'''
Remark: Recursive function

Think the problem as a Fibonacci:
1. If n == 1, only one way to reach the top
2. If n == 2, a step of 2 or two steps of 1, two ways to climb to the top

Now we can think of the problem as how many ways to get to n-1 and n-2 
'''


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution(object):

    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
