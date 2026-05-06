class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        mem = {x: 1 for x in nums}

        res = 1

        for key in mem:
            if key-1 in mem:
                mem[key] = mem[key-1] + 1
                res = max(res, mem[key])

        return res