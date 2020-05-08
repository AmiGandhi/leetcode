# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums):
        d = {}

        for char in nums:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for k,v in d.items():
            if v >= len(nums)/2:
                return k

if __name__ == "__main__":
     nums = [3,2,3]
     print(Solution().majorityElement(nums))