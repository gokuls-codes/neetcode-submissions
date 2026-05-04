class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mem = Counter(nums)
        ptr = 0

        for key in range(3):
            for i in range(mem[key]):
                nums[ptr] = key
                ptr += 1 