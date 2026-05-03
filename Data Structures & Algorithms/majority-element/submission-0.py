class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mem = Counter(nums)
        req = len(nums) / 2

        for key in mem:
            if mem[key] > req: return key