class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(c for c in s if c.isalnum())
        lowered_str = new_str.lower()
        return lowered_str == lowered_str[::-1]
        