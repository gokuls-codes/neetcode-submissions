class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)

        minBuy = prices[0]
        
        for i in range(1, n):
            res = max(res, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])

        return res