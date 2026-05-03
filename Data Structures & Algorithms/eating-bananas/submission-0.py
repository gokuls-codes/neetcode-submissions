class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPossible(rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            
            if hours <= h:
                return True
            
            return False

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
