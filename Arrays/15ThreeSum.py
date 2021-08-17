class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea: to turn the three sum problem into a 2 sum problem 
        # we sort the array first so we can both avoid the duplicates and using 2 pointer method to solve for the 2 sum
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue # if we encounted the same fixed index, we need to skip it
            lp, rp = i + 1, len(nums) -1
            while lp < rp:
                currSum = v + nums[lp] + nums[rp]
                if currSum > 0:
                    rp -= 1
                elif currSum < 0:
                    lp += 1
                else:
                    res.append([v,nums[lp],nums[rp]])
                    lp += 1
                    # if we encounter the same left pointer, we also need to skip it so the result have no duplicate
                    while nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1  
        return res
