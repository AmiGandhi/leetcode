# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        temp=[]
        
        while 1:
            for x in str(n):
                n = int(x)%10
                sum += int(n)**2
            n=sum
            if n in temp:
                break
            else:
                temp.append(n)
            sum=0
        
        if n==1:
            return True
        else:
            return False

if __name__ == "__main__":
    n=19
    print(Solution().isHappy(n))