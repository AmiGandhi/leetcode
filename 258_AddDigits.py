# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# Solution Using loop:
class Solution:
    def addDigits(self, num: int) -> int:
        if(num<10):
            return num
        sum=0
        temp=[]
        while len(str(num))>1:
            for x in str(num):
                sum += int(x)
            num=sum
            if(num in temp):
                break
            else:
                temp.append(num)
            sum=0
        return num
    
    def addDigitsWithoutLoop(self, num: int) -> int:
        if num == 0: 
            return 0
        else:
            return (num - 1) % 9 + 1  

if __name__ == "__main__":
    n=38
    print(Solution().addDigitsWithoutLoop(n))