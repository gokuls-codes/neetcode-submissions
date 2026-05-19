class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        
        while i < j:
            if s[i] != s[j]:
                skipI = s[i+1:j+1]
                skipJ = s[i:j]
                return skipI == skipI[::-1] or skipJ == skipJ[::-1]
            i += 1
            j -= 1
        
        return True