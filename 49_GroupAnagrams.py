# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs):

        dict = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in dict:
                dict[sortedWord] = [word]
            else:
                dict[sortedWord].append(word)
        return list(dict.values())
        
        #  OR as below - faster approach
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))