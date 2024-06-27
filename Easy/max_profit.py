# Leetcode 121 Best Time to Buy and Sell Stocks

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf") # set min_price to infinity
        
        for price in prices: # loop through and keep track of the min price as you traverse
            if price < min_price:
                min_price = price
            elif max_profit < price - min_price: # update max_profit if the previous one is less than the current one
                max_profit = price - min_price
        
        return max_profit