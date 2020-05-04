# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

class Solution:
    def reverseStr(self, s, k):
        a = list(s)
        if len(s)<k:
            return s[::-1]
        for i in range(0, len(a), 2*k):
            a[i:i+k] = a[i:i+k][::-1]
        return "".join(a)

if __name__ == "__main__":
    s="abcdefg"
    k=2
    print(Solution().reverseStr(s,k))   