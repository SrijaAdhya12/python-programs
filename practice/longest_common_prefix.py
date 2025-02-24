# Write a function to find the longest common prefix string amongst an array of strings.

"""min: min is a builtin function that takes an iterable and an optional parameter key that takes a function(can also be an annonymous function, also be name of function) to compare each value of the iterable and find out the minimum most value"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        for i,char in enumerate(shortest_word):
            for word in strs:
                if word[i] != char:
                    return shortest_word[:i]
        return shortest_word
        