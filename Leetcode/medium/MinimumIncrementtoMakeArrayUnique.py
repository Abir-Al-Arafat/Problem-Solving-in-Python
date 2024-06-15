# 945. Minimum Increment to Make Array Unique

# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

# Return the minimum number of moves to make every value in nums unique.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].
# Example 2:

# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

from typing import Counter, List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        output = 0
        for idx in range(len(nums)):
            if numsCount[nums[idx]] > 1:
                temp = nums[idx]
                while temp in numsCount:
                    temp += 1
                    output += 1
                numsCount[nums[idx]] -= 1
                nums[idx] = temp
                numsCount[temp] = 1
        return output
    
    def minIncrementForUnique2(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        for right in range(1, len(nums)):
            if nums[right-1] >= nums[right]:
                output += 1 + (nums[right-1] - nums[right])
                nums[right] = nums[right-1] + 1
        return output