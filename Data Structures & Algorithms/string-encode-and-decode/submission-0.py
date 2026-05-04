class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        lens = [len(s) for s in strs]
        res = ""

        for l in lens:
            res += str(l)
            res += ','
        
        res += '#'
        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        lens, res, i = [], [], 0
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            lens.append(int(curr))
            i += 1
        i += 1

        for l in lens:
            res.append(s[i:i + l])
            i += l
        
        return res
