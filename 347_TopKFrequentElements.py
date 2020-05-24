# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.

#  refered logic from - https://www.youtube.com/watch?v=9sa3mx07XY8
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        kmost = []
        
        for num, freq in freq_dict.items():
            if len(kmost)<k:
                heapq.heappush(kmost, (freq,num))
            else:
                min_freq, min_num = heapq.heappop(kmost)
                
                if freq>min_freq:
                    heapq.heappush(kmost, (freq,num))
                else:
                    heapq.heappush(kmost, (min_freq,min_num))
        return [n for _,n in kmost]

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))