# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_items = sorted(count.items(), key=lambda x: x[1])
        sorted_keys = [item[0] for item in sorted_items[::-1][:k]]
        return sorted_keys
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, val in count.items():
            freq[val].append(key)

        for idx in range(len(freq)-1, 0, -1):
            for item in freq[idx]:
                result.append(item)
                if len(result) == k:
                    return result