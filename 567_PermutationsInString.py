# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
                
        length_of_s1, length_of_s2 = len(s1), len(s2)
        if length_of_s1 > length_of_s2:
            return False
        
        s1_counter = Counter(s1)
        window_counter = Counter()
        
        for i,c in enumerate(s2):
            window_counter[c] += 1
            
            if i >= length_of_s1:
                element_on_left = s2[i-length_of_s1]
                if window_counter[element_on_left] == 1:
                    del window_counter[element_on_left]
                else:
                    window_counter[element_on_left] -= 1
                
            if window_counter == s1_counter:
                return True
        return False

if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1,s2))