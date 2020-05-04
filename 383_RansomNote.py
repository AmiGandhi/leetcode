# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
    def canConstructUisngCollections(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

if __name__ == "__main__":
    ransomNote = "a"
    magazine="b"
    print(Solution().canConstruct(ransomNote,magazine))