# Edit Distance | [Link](https://leetcode.com/problems/edit-distance/)  
## Idea
   This solution is heavily influenced by the [top-voted discussion post](https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition), which was really helpful and strongly recommended to read.

   The very first approach is try to solve this problem in brute force. Without any constraint, how could we solve the problem? If we take a detailed look, it's not hard to find out that the problem can be viewed in this way:
* for every index pair of word1 and word2, if they are the same, we can just consider the rest of them
* if an action is needed, we want to find the minimum action to make them the same
    
   thus, the logic for the editing part is done and can be implemented by
   ```python
    if word1[0] == word2[0]:
        return minEdit(word1[1:],word2[1:])
    else:
        insert = 1 + minEdit(word1,word2[1:])
        delete = 1 + minEdit(word1[1:],word2)
        replace = 1 + minEdit(word1[1:],word2[1:])
        return min(insert,delete,replace)
   ```
   however, it's also important to consider the base cases as well--and it's not that complicated. We can simply return the length of the other word if one word ends up empty. Taking that into consideration, we can have the naive approach of the solution done
   ```python
    def minDistance(self, word1: str, word2: str) -> int:
        # base case, when one word is empty, just insert the rest
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        # otherwise, we need make some chanegs
        else:
            # insert first char of word2 to word1
            insert = 1 + self.minDistance(word1,word2[1:])
            delete = 1 + self.minDistance(word1[1:],word2)
            replace = 1 + self.minDistance(word1[1:],word2[1:])
            return min(insert,delete,replace)
   ```
   while this solution would work, the amount of recursive call would be such a waste of memory and time. Also, your interviewer would definitely not be satisfy with this. Thus, a way to optimize it is very neccessary. 

   It turns out that the result of some sub-problems can be reused in later calculation. For instance, if we already found out that `'hello'` and `'ell'` needs 2 changes, during the calculation of finding the min edit of `'helloworld'` and `'bell'`, the result of the previous sub-problem would definitely be useful and we don't have to re-calculate them. 

   So starting from our base case that an empty word would require the length of the other word as the min edit, we can build up the dp array.
   ```python
   # initialization
    m,n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    # dp[i][j] =>  min edit distance for word1[:i] and word2[:j]
    # base cases
    for i in range(m+1): # if one word is empty, its min edit is the len of other
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
   ```
   during process of building up, the problem still have to face 2 options: when the 2 characters of the given index is the same and when they are different.
   ```python
   # if they are the same, we can just worry about the rest
   if word1[i] == word2[j]:
       dp[i][j] = dp[i-1][j-1]
    else: # we have to make an edit, but the one with the min edit distance
        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
                         #delete        insert      replace
   ```
   and that should conclude the whole construction of the dp array where we memoized the results of each sub-problem. Putting it all together, we have the solution
   ```python
   class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        return dp[m][n]
        
   ```
   Where time complexity and space complexity should both be O(mn)
