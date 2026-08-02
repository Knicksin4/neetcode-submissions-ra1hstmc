class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxp = 0

        while l < r and r < len(prices):
            profit = (prices[r] - prices[l])
            maxp = max(maxp, profit)

            if prices[r] < prices[l]:
                l = r
            
            r += 1

        return maxp
        