# Find Minimum in Rotated Sorted Array | [Link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
# Idea
We can use binary serach to find the interval that is sorted and contains the smallest element then return it.
```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right  = 0, len(nums) -1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]: # not supposed to happen
                left = mid + 1 # not inclusive since it is greater than something
            elif nums[left] > nums[mid]:
                right = mid # inclusive because this might be the min
            else: # the interval we are dealing is already sorted
                return nums[left]
        return nums[left]
```