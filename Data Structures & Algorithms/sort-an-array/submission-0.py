class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(l, r):
            if l == r: return [nums[l]]
            mid = (l + r) // 2
            left = helper(l, mid)
            right = helper(mid + 1, r)

            res = []
            i, j = 0, 0
            leftLen, rightLen = mid - l + 1, r - mid

            while i < leftLen and j < rightLen:
                if left[i] < right[j]: 
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < leftLen:
                res.append(left[i])
                i += 1
            
            while j < rightLen:
                res.append(right[j])
                j += 1
            
            return res

        return helper(0, len(nums) - 1)