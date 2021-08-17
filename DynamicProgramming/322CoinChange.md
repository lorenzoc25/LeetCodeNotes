# Coin Change | [Link](https://leetcode.com/problems/coin-change/)  
## Idea
   Since we are asked to give out the minimum number of coins needed to make up for a certain amount, the very first thing comes to mind is that we could list all 
   the possiblities of coins.  
   So if we have the amount of 12 and are provided with coin option of `[1, 2, 5]`, we can attempt to find the solution by using all the possible coins avaliable:  
   - use a 1, then we have an amount of 12 - 1 = 11, the total coins needed will be 1 + whaterver number of coins we need for amount 1
   - use a 2, we have amount of 12 - 2 = 10, the total coins needed will be 1 + whaterver number of coins we need for amount 10
   - use a 5, amount will be 7 and the total coins needed will be 1 + whaterver number of coins we need for amount 7
  
   It's not hard to find out that if we want to solve the problem in this way, we could break the large problems into many smaller ones. So like in this example, the
   optimal solution should be using 3 coins of 5, 5, and 2, and the process should be something like this(order does not matter):  
   ```
   choose 2 --> find the min coins that can make up to 10
                        +-----------------> choose 5 --> find the min coins that can make up to 5
                                                                  +-----------------> choose 5 --> found the amount, return 
  ```
                                                                  
   we could use recursion to finish the problem, but the amount of calls we need to make is huge. Instead, we can use dynamic programming to store the results of every amount of coins, which would make the whole process much more efficient.
   So how should we start it? If we want to store all the result from 0 to amount, we need an array of amount + 1 slots.  
   For each amount, the max number of coins you can use to make up the amount will be amount(i.e. use 12 ones to make up one) and we always know that if amount is 0 we 
   can return 0, so we can initialize the dp array as 
   ```python
   dp = [amount]*(amount+1)
   dp[0] = 0
   # dp[i] = j ==> for amount i, the minimum number of coins will be j
   ```
   however, this could lead to a bug. What if the coin with value one is not provided? We also need to consider the sitaution that if an amount cannot be made. Thus,
   we should initialize the array to a number that is larger than amount so we can make sure the program works as intented. We can simply do amount + 1 instead of 
   amount because we know that the maximum possible number that our program could generate will be amount for each slot, so that will serve the purpose.  
   Then, we can write the logic for the decision for each slot.
   
   for each slot, if I can use a coin in the avaliable coins, I'll change that slot's value to the smaller value between it's current value or 1 + the minimum number of coins for value (current amount - current coin value)
   
   in code, it will look like`dp[amt] = min(dp[amt], 1 + dp[amt - coin])`
   
   Then, putting it all together, we can get our solution.
   ```python
   class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [amount + 1] *(amount + 1) # worst case would be amount, so amount + 1 could represent infinity
        dp[0] = 0
        # dp[i] --> the minimum number of coins of amount i
        # meaning of dp[i] = j : i --> amount, j == numCoins needed
        for i in range(amount+1):
            # so i is the current amount
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i],dp[i-coin] + 1)
        if dp[amount] == amount + 1: # never changed
            return -1
        return dp[amount]
   ```

