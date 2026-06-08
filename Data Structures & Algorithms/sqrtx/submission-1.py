class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x//2 + 1):
            if (i+1)*(i+1) > x:
                return i
        return 1