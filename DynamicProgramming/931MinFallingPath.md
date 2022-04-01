# Minimum Falling Path Sum | [Link](https://leetcode.com/problems/minimum-falling-path-sum/)

## Idea
This question is similar to question 64, [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/), which itself is similar to question 62 Unique Path and its solution can be checked [here](https://github.com/lorenzoc25/LeetCodeNotes/blob/main/DynamicProgramming/62UniquePath.md). Since those questions are all so similar, I don't plan to elaborate on expalining the logic for every one of them. But if you are curious, I will provide a solution to 64 in addition to this problem's solution at the end of the page.  

The overall idea is just to use a DP table to list and store all the possible ways to get a "falling path" as the quesiton described. After we list them, we can just return the minimum value from the last row since that will gurante to be the min falling path sum.
## Code
```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[101]* n for i in range(m)] # create a dp table with the same dimension
        
        # initialize the first row of dp to the matrix's first row
        for i in range(n):
            dp[0][i] = matrix[0][i]
        # calculate the actual dp table
        for i in range(1,m): # starting from the second row since we already initialized the first row
            for j in range(n):
                if i > 0 and 0 < j < n - 1: # can come from top, top left or top right
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
                elif j == n-1: # can come from top and top left
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1])
                elif j == 0: # can come from top and top right
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
        return min(dp[-1])
```

## Solution to [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[101]*cols]*rows
        dp[0][0] = grid[0][0]
        for i in range(rows):
            for j in range(cols):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
                elif j > 0: # i == 0, top row
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif i > 0: # j == 0, left col
                    dp[i][j] = grid[i][j] + dp[i-1][j]
        return dp[rows-1][cols-1]
```
