# 1248. Count Number of Nice Subarrays

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        mid = 0
        oddCount = 0
        result = 0

        for right in range(len(nums)):
            if self.isOdd(nums[right]):
                oddCount+=1

            while oddCount > k:
                if self.isOdd(nums[left]):
                    oddCount-=1
                left += 1
                mid = left

            if oddCount == k:
                while not self.isOdd(nums[mid]):
                    mid += 1
                result += (mid - left) + 1
            

        return result
    
    def isOdd(self, num: List[int]) -> bool:
        if num%2==1:
            return True
        return False