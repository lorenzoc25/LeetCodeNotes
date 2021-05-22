class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # idea: to traverse from the back of the array and see if we can finally reach the starting position
        lastIndex = len(nums) - 1
        # starting from the second last index
        i = lastIndex - 1
        while i >= 0:
            # if we can reach the lastIndex from the current index i, the current index i will be the last index
            if nums[i] + i >= lastIndex:
                lastIndex = i
            i -= 1
        # successfully reached the initial position from the last position
        return lastIndex == 0
