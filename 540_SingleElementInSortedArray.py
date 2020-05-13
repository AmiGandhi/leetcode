# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

# Example 1:

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: [3,3,7,7,10,11,11]
# Output: 10
 
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution:
    def singleNonDuplicate(self, nums):

#         Below solution takes O(n) time
#         d={}
#         for x in nums:
#             if x in d:
#                 d[x] += 1
#             else:
#                 d[x] = 1
         
#         for k,v in d.items():
#             if d[k] == 1:
#                 return k

#       Binary Search method - O(logN) time
        minimum=0
        maximum= len(nums) - 1

        while minimum<maximum:
            middle = (minimum+maximum) // 2
            # print(middle)
            if nums[middle] != nums[middle-1] and nums[middle] != nums[middle+1]:
                return nums[middle]
            else:
                if nums[middle] == nums[middle-1]:
                # Even number
                    if (middle-1)%2:
                        maximum = middle-2
                    else:
                        minimum = middle+1
                elif nums[middle] == nums[middle+1]:
                  # Odd number
                    if middle%2:
                        maximum = middle-1
                    else:
                        minimum = middle+2

        return nums[minimum]

if __name__ == "__main__":
    nums = [1,1,2,3,3,4,4,8,8]
    print(Solution().singleNonDuplicate(nums))