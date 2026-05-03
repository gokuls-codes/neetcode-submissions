class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for word in strs:
            currKey = "".join(sorted(list(word)))
            mem[currKey].append(word)

        return list(mem.values())