# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.

class Solution:
    def removeDuplicates(self, nums):
        new_index = 1
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[new_index] = nums[i+1]
                new_index+=1
        return new_index

if __name__ == "__main__":
    nums=[0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))