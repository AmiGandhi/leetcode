# Given a positive integer num, write a function which returns True 
# if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Example 2:

# Input: num = 14
# Output: false
 

# Constraints:

# 1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
         # Binary Search
#         if num<0:
#             return False
        
#         minimum = 0
#         maximum = num
#         while minimum < maximum:
#             middle = (minimum+maximum)//2
            
#             midSquare = middle ** 2
            
#             if num==midSquare:
#                 return True
#             elif num<midSquare:
#                 maximum -= 1
#             else:
#                 minimum += 1

#         return any( num==x**2 for x in range(minimum,maximum+1) )

#         Newton Method
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num