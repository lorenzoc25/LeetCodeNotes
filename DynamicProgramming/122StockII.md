# 122 Best Time to Buy and Sell Stock II | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
## Idea
We want to create a dp array and store all the information (in this case, the maximum profit) based on choice. The final slot will be the desired anser.
## Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]* 2 for i in range(len(prices))]
        # dp[i][0] => at ith day, the profit I can get by not holding a stock
        # dp[i][1] => at ith day, the profit I can get by holding a stock
        for i in range(len(prices)):
            # if I don't have a stock at day i
            if i == 0: # This is the base case
                # dp[0][0] should be 0, but we already initialized the array to be 0
                # at the begining, we can't have any stock from the previous day, so we have to "buy" it, the profit is thus 0 - price[0] which is -price[0]
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], # I don't have a stock at i-1
                           dp[i-1][1] + prices[i] # I sold my stock holding
                          )
            # if I have a stock at day i
            dp[i][1] = max(dp[i-1][1], # I didn't sell my stock at i-1
                           dp[i][0] - prices[i] # I bought a stock at i
                          )
        return dp[-1][0]
        
                
```