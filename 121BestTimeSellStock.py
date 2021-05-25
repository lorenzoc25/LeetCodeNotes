class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first, create a minimum price that we've encountered
        minPrice = 10001
        # when we check the current profit and record it
        maxProfit = 0
        for price in prices:
            minPrice = min(price, minPrice)
            # current price - minPrice --> current profit that we can make
            maxProfit = max(price-minPrice, maxProfit)
        return maxProfit
