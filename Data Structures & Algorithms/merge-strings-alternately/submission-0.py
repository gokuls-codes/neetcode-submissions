class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        res = ""

        while i < min(m, n) and j < min(m, n):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        res += word1[i:m]
        res += word2[j:n]

        return res