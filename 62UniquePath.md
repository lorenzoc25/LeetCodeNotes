# Unique Path | [Link](https://leetcode.com/problems/unique-paths/)
## Idea
  We want to break down the whole problem into small pieces and use dynamic programming to solve it. If we are given M rows and N columns and are asked how many paths can there be for us to reach, we can find how many paths we can get to the previous step to the destination and sum them. 
  
  So, say we want to arrive at coordinate (a,b) and we are only allowed to go right and down if possible, then we know to get to (a,b), the previous step before we
  arrive at (a,b) has either to be (a-1,b) or (a,b-1), and that rule applies for every coordinate in the grid.  
  
  Thus, we can have our own algorithm to form a grid to find the number of ways to get to (m,n). Let's denote it f[m][n]
  - for the coordinates that can only be reached from going down (the leftmost column), f[m][n] = f[m-1][n]
  - for the coordinates that can only be reached from going right (the topmost row), f[m][n] = f[m][n-1]
  - for the coordinates that can be reached from both going down and going right, f[m][n] = f[m-1][n] + f[m][n-1]  
  
  After processing all the steps, we will get a matrix of numbers that is m x n, and matrix[m-1][n-1] will be our final anser, as it represents f[m][n]
## Code
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if j == 0: # j = 0, at left col, can only reach here by go down
                    dp[i][j] = dp[i-1][j]
                elif i == 0: # i = 0, at top row, can only reach here by go right
                    dp[i][j] = dp[i][j-1]
                else: # not at the corner or edge, can go both right and down
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
```
