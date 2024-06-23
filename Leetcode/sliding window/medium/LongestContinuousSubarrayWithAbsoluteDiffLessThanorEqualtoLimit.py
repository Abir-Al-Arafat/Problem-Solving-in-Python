# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        answer = 0
        minQueue = deque([])
        maxQueue = deque([])

        for right in range(len(nums)):
            while minQueue and minQueue[-1] > nums[right]:
                minQueue.pop()
            minQueue.append(nums[right])

            while maxQueue and maxQueue[-1] < nums[right]:
                maxQueue.pop()
            maxQueue.append(nums[right])

            if maxQueue[0] - minQueue[0] <= limit:
                answer = max(answer, right-left+1)
            else:
                if minQueue[0] == nums[left]:
                    minQueue.popleft()
                if maxQueue[0] == nums[left]:
                    maxQueue.popleft()
                left+=1
        
        return answer