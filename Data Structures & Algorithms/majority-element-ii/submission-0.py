class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mem = Counter(nums)
        return [x for x in mem if mem[x] > len(nums)//3]