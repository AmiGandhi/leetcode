# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s):
        d = {}
        keys = []

        if not s:
            return -1
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for k,v in d.items():
            if v == 1:
                keys.append(k)

        for i in range(len(s)):
            if keys:
                if keys[0] == s[i]:
                    return i
            else:
                return -1

    def better_solution(self,s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

if __name__ == "__main__":
    s = "leetcode"
    print(Solution().better_solution(s))