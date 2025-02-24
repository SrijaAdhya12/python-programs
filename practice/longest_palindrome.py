# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.


from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = Counter(s).values()
        even_sum = sum(i for i in frequency if not i % 2)
        odds = [i for i in frequency if i % 2]
        middle = max(odds, default=0)
        if middle: odds.remove(middle)
        odd_sum = sum(i-1 for i in odds)
        return odd_sum + middle + even_sum
        