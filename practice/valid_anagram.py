class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_str1 = sorted(s.lower())
        my_str2 = sorted(t.lower())
        return my_str1 == my_str2

        