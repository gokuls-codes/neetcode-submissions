class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        n = len(nums)

        for i in range(n):
            if mem.get(nums[i], -1) != -1:
                prev = mem[nums[i]]
                if i - prev <= k: return True
            mem[nums[i]] = i

        return False
        