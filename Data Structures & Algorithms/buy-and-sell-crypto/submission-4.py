class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 101
        
        for price in prices:
            
            if price - min_price > max_profit:
                max_profit = price - min_price

            if price < min_price:
                min_price = price
        return max_profit


        # two pointers
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > maxP:
                maxP = diff
            else:
                l = r
            r += 1
        return maxP
