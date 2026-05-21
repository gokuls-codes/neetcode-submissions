class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        mem = [prices[0]]
        for i in range(1, n):
            mem.append(min(mem[-1], prices[i]))
        
        for i in range(1, n):
            res = max(res, prices[i] - mem[i-1])

        return res