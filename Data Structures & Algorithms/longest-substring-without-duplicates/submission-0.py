class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        res = 0
        n = len(s)
        start = 0

        for i in range(n):
            while s[i] in curr:
                curr.remove(s[start])
                start += 1
            curr.add(s[i])
            res = max(res, i-start+1)
        
        return res