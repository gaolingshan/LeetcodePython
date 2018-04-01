'''
690. Employee Importance
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

'''

'''
Tag: hashtable

Thoughts:
1. Create a dictionary with keys = unique employee IDs 
and values = employee info
2. Pass the dictionary to calcImportance
3. Define a recursive calcImportance function to sum up the importance scores
of subordinates
'''


"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# Version 1: Recursion
class Solution:

    def calcImportance(self, id):
        res = self.d[id].importance

        for sub_id in self.d[id].subordinates:
            res += self.calcImportance(sub_id)
        return res

    def getImportance(self, employees, id):
        """
        :type employees: Employee list
        :type id: int
        :rtype: int
        """
        d = {}
        for i in range(len(employees)):
            d[employees[i].id] = employees[i]

        self.d = d  # add dictionary to self
        return self.calcImportance(id)

# Version 2: While loop + stack
class Solution():

    def calcImportance(self, id):
        res = self.d[id].importance

        for sub_id in self.d[id].subordinates:
            res += self.calcImportance(sub_id)
        return res

    def getImportance(self, employees, id):
        """
        :type employees: Employee list
        :type id: int
        :rtype: int
        """
        d = {}
        for i in range(len(employees)):
            d[employees[i].id] = employees[i]

        res = d[id].importance
        stack = d[id].subordinates

        # while stack is not empty
        while stack:
            temp = stack.pop()
            res += d[temp].importance
            stack.extend(d[temp].subordinates)
        return res


aa = Solution()
print(aa.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))
