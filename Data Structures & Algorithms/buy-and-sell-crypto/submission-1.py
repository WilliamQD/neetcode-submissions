class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 101

        for price in prices:
            if price < min_price:
                min_price = price
            
            else:
                max_profit = max(price - min_price, max_profit)
        
        return max_profit

