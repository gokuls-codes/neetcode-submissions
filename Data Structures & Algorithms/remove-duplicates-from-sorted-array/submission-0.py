class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ptr = 0
        curr = 0
        prev = None

        while ptr < n:
            if nums[ptr] != prev:
                nums[curr] = nums[ptr]
                curr += 1
                prev = nums[ptr]

            ptr += 1

        return curr