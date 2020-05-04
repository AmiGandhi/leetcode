# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        left, right = 0, len(s)-1
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right -1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        return ''.join(s)

if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseVowels(s))