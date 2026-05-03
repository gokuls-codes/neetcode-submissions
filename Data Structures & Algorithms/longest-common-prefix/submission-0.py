class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        currPrefix = strs[0]

        for i in range(n):
            if strs[i].startswith(currPrefix): continue
            while not strs[i].startswith(currPrefix) and currPrefix != "":
                currPrefix = currPrefix[:-1]
            if currPrefix == "": return ""

        return currPrefix