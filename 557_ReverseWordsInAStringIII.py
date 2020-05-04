# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution:
    def reverseWordsUsing2Pointers(self, s):
        s = s.split(' ')
        s=list(s)
        reversed_word_list=[]
        for word in s:
            word=list(word)
            left, right = 0, len(word)-1
            while left<right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            reversed_word_list.append("".join(word))
        print(reversed_word_list)
        result = ""  
        for elem in reversed_word_list:  
            result = result + elem + " "
        return result.rstrip()
        
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]
        
if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))