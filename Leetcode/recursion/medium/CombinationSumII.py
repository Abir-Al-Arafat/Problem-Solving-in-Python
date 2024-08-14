# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def backtrack(idx, currentCombo, total):
            if total == target:
                output.append(currentCombo.copy())
                return
            
            if total > target or idx >= len(candidates):
                return

            currentCombo.append(candidates[idx])
            backtrack(idx+1, currentCombo, total + candidates[idx])
            currentCombo.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            
            backtrack(idx+1, currentCombo, total)
        backtrack(0, [], 0)
        return output