# 1046. Last Stone Weight

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1

import heapq
from typing import List

class Solution:
    # sorting
    def lastStoneWeightSorting(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            stones[len(stones)-2] = stones[len(stones)-1] - stones[len(stones)-2]
            stones.pop()
        return stones[0]
    # maxheap
    def lastStoneWeightMaxHeap(self, stones: List[int]) -> int:
        for idx in range(len(stones)):
            stones[idx] = -stones[idx]
        
        heapq.heapify(stones)

        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, y-x)
        return -stones[0] if stones else 0

# stones = [2,7,4,1,8,1]
stones = [1]
stones.sort()
print(stones)

solulu = Solution()
print(solulu.lastStoneWeight(stones)) 