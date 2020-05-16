# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution 
# using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums):
        
        total_sum = max_sum = nums[0]
        
        for i in nums[1:]:
            total_sum = max(i, total_sum+i)
            max_sum =  max(max_sum, total_sum)
        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))