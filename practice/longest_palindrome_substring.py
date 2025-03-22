class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(strng):
            return strng == strng[::-1]

        longest_word =""
        for i,v in enumerate(s):
            for j in range(i, len(s)+1):
                substring = s[i:j]
                if is_palindrome(substring) and len(substring) > len(longest_word):
                    longest_word = substring
        return longest_word
            