class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        
        letters = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"))
        i,j = 0, n-1

        while i < j:
            while i < j and s[i] not in letters:
                i += 1
            while i < j and s[j] not in letters:
                j -= 1
            
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True
            