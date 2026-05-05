class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProds = [1]
        sufixProds = [1]
        n = len(nums)

        for i in range(1, n):
            prefixProds.append(nums[i-1] * prefixProds[-1])
        for i in range(n-2, -1, -1):
            sufixProds.append(nums[i+1] * sufixProds[-1])
        
        print(prefixProds, sufixProds)
        return [prefixProds[i] * sufixProds[n-i-1] for i in range(n)]