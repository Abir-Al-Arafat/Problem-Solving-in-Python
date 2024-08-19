# 2418. Sort the People

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

from typing import List

class Solution:
    # Time: O(n^2)
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)-1):
            for j in range(i+1, len(names)):
                if heights[j] > heights[i]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]
        
        return names
    # Time: O(n + nlogn)
    def sortPeople2(self, names: List[str], heights: List[int]) -> List[str]:
        heightNameMap = {}

        for name, height in zip(names, heights):
            heightNameMap[height] = name

        idx = 0
        for height in reversed(sorted(heights)):
            names[idx] = heightNameMap[height]
            idx += 1

        return names
