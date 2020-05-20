# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False
        if len(s)==0 and len(t)==0:
            return True

        # return Counter(s) == Counter(t)
        # OR as below
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s,t))