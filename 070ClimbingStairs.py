'''
70. Climbing Stairs
Difficulty: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''

'''
Remark: 
1. Recursive function

Think the problem as a Fibonacci:
1. If n == 1, only one way to reach the top
2. If n == 2, a step of 2 or two steps of 1, two ways to climb to the top

Now we can think of the problem as how many ways to get to n-1 and n-2 
A simple tweek to save some run time:
As the function runs recursively, we can save the results of f(n-1), f(n-2)... in an array.

2. For loop

A more general approach to solve this problem, or dynamic programming (dp) problems, is:
1. 确定转移方程 transition functions
2. 确定状态 states
3. 边界条件 boundaries: start states (usually are 0 and/or 1 states), end states (what the problem asks for)

先解决小问题，推到转移方程，解决大问题
'''

# 1. Recursion


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

# 2. For loop


class Solution(object):

    def climbStairs(self, n):
        # state 0 and state 1, there's only one way of doing so
        res = st0 = st1 = 1
        if n > 1:
            for _ in range(1, n):
                res = st1 + st0
                st0 = st1
                st1 = res
        return res
