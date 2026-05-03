class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mem1 = Counter(s)
        mem2 = Counter(t)

        for i in range(26):
            ch = chr(ord('a') + i)
            if mem1[ch] != mem2[ch]:
                return False

        return True