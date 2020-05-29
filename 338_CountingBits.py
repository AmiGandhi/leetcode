# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution:
    def countBits(self, num):
        # result = [0]
        # for i in range(1, num+1):
        #     result.append(result[i>>1] + int(i&1))
        # return result
        
#         OR
        # res=[0]
        # for _ in range(ceil(log(num + 1, 2))):
        #     res+=[i+1 for i in res]
        # return res[:num+1]
        
#        OR 
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]

if __name__ == "__main__":
    num= 2
    print(Solution().countBits(num))