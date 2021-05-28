# fining the maximum sum of an array's subarray
# idea is easy, we keep the current sum on track, and if we ever encounter a number larger than the current sum, we ignore that 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0: # after we added the previous number, if the whole sum is negative, we disregard that
                curr_sum = 0
            curr_sum += n
            maxSub = max(maxSub, curr_sum) # check if the current sum is the biggest sub sum
        return maxSub 
