class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        resPointer = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == val: continue
            nums[resPointer] = nums[i]
            resPointer += 1

        return resPointer