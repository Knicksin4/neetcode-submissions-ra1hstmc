class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatest = 0

        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            greatest = max(greatest, profit)

        return greatest
        