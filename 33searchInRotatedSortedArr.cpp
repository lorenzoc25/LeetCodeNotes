/*
    got wrong answer 3 times:
    first time: after finding the pivot and determining which side of the array, only thought of updating the left bound but not the right bound (not sure if that's the real cause tho)
    second time: after finding the pivot and determining which side of the array, forgot to check the right bound (only did target > nums[start] but not target < nums[right])
    third time: didn't make the boundary inclusive, should be inclusive

*/

int search(vector<int> &nums, int target)
{
    // find the pivot point first
    int left = 0, right = nums.size() - 1;
    while (left < right)
    {
        int mid = (left + right) / 2;
        if (nums[mid] > nums[right]) // if the middle element is greater than the end, the arr in the current frame
                                     // is not sorted
        {
            left = mid + 1;
        }
        else
        {
            right = mid; // reduce the search size to half
        }
    }

    // now, left would equal to the pivot point of the arr
    int start = left;
    left = 0;
    right = nums.size() - 1;
    // determine which side of the arr we are gonna to search
    if (target >= nums[start] && target <= nums[right])
    {
        left = start;
    }
    else
    {
        right = start;
    }

    // regular binary search
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
    }
    return -1;
}