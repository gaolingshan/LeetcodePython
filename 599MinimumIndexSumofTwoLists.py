'''
599. Minimum Index Sum of Two Lists
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

'''

'''
Tag: hashtable

Thought: 
1. create a hashtable to store list1 and its element indices.
2. iterate list2, if element also in list1, check the sum of the indices
3. If sum equal, append to result list, if smaller, then create a new list 
with this restaurant name
'''

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i, rest in enumerate(list1):
            d[rest] = i

        max_sum = 2000 # given the length of both lists will be in the range
        # in [1, 1000]
        res = []

        for i, rest in enumerate(list2):
            if (rest in d) and (d[rest] + i < max_sum):
                max_sum = d[rest] + i
                res = [rest]
            elif (rest in d) and (d[rest] + i == max_sum):
                res.append(rest)

        return res

aa = Solution()
print(aa.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))