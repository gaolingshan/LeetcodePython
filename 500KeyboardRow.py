'''
500. Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''

'''
Tag: hashtable

Thoughts:
1. Create a list of sets where each set contains one row of letters on the keyboard. -> mother set
2. Iterate over the word list, convert each word to a set, compare this set with mother set
2. Iterate over the word list, convert each word to a set, compare this set with mother set.
'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
             {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
             {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]
        res = []
        for i in range(len(words)):
            w_set = set(words[i].lower())
            if w_set <= d[0] or w_set <= d[1] or w_set <= d[2]:
                res.append(i)
        return [words[i] for i in res]