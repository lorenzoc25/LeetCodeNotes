'''
 got wrong answer 2 times
  first time: forgot to check the negative coordinate(python support negative index accessing for arrays)
  second time: false understanding of x and y accessing of array which leads to pass in the wrong parameter of bfs

'''

class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        aBound = len(grid)
        bBound = len(grid[0])
        # direction purpose
        a_dir = [1,0,-1,0]
        b_dir = [0,1,0,-1]
        # idea: if we encouter an island, increase the count and turn all of this island into water
        def dfs(grid,a,b):
            # invalid coordinate
            if a < 0 or b < 0 or a >= aBound or b >= bBound:
                return 
            if grid[a][b] == '0': # water
                return 
            else:
                grid[a][b] = '0' # mark current as visted
                for i in range(4):
                    dfs(grid,a+a_dir[i],b+b_dir[i])
                    
        # traverse thru the grid, if we found an island, turn it back to 0 and increment the count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid,i,j)    # to check the surronding to see if this spot is connected to land
                    count += 1
        return count