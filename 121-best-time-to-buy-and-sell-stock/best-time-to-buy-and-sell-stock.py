class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        low_price = prices[0]
        for price in prices:
            if price < low_price:
                low_price = price
            maxP = max(maxP, price - low_price)
        
        return maxP