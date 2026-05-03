class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = defaultdict(list)
        n = len(nums)

        for i in range(n):
            req = target - nums[i]
            if mem[req]:
                return [mem[req][0], i]

            mem[nums[i]].append(i)