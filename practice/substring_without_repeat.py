class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = ""
        for i,v in enumerate(s):
            for j in range(i,len(s)+1):
                substring = s[i:j+1]
                if len(set(substring)) == len(substring) and len(substring) > len(max_substring):
                    max_substring = substring
        return len(max_substring)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        max_len = 0
        for i, v in enumerate(s):
            while v in charset:
                charset.remove(s[l])
                l += 1
            charset.add(v)
            max_len = max(max_len, i - l + 1)
        return max_len

                
        