# jump game i 
class JG1:
# forward approach
    def canJump1(self, nums: List[int]) -> bool:
        maxDistance = 0
        for i in range(len(nums)):
            currStep = nums[i]
            if i <= maxDistance:
                maxDistance = max(maxDistance, i + currStep)
        return maxDistance >= len(nums)-1
      
 # backward approach
    def canJump(self, nums: List[int]) -> bool:
        # idea: to traverse from the back of the array and see if we can finally reach the starting position
        lastIndex = len(nums) - 1;
        # starting from the second last index
        i = lastIndex - 1
        while i >= 0:
            # if we can reach the lastIndex from the current index i, the current index i will be the last index
            if nums[i] + i >= lastIndex:
                lastIndex = i;
            i -= 1
        return lastIndex == 0
            

# jump game ii
class JG2:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        max_reachable_from_curr, max_reachable = 0,0
        for i in range(len(nums)-1):
            max_reachable = max(nums[i]+i,max_reachable)
            if i == max_reachable_from_curr:
                # if i is equal to the actual max step that we can reach, we have to take a step
                steps += 1
                # max reachable distance from current is updated. 
                # since the region from the previous place we need to jump to the max reachable distance from there can all be jumped within 1 jump,
                # then within one jump that we've already took plus any other jump from that region, we can reach the max_reachable index.
                max_reachable_from_curr = max_reachable
        return steps
                
