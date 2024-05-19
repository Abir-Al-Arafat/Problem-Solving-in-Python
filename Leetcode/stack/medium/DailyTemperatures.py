# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for idx in range(len(temperatures)):
            if idx+1 < len(temperatures) and temperatures[idx+1] > temperatures[idx]:
                answer.append(1)
            else:
                wait = idx+1
                while wait < len(temperatures) and temperatures[idx] >= temperatures[wait]:
                    if temperatures[idx] < temperatures[wait]:
                        answer.append(wait-idx)
                    wait+=1
                if wait < len(temperatures) and temperatures[wait] > temperatures[idx]:
                    answer.append(wait-idx)
                else:
                    answer.append(0)
                
        if len(answer) < len(temperatures):
            while len(answer) != len(temperatures):
                answer.append(0)
        
        return answer
    
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[index] > stack[-1][0]:
                lowTemp, lowTempIdx = stack.pop()
                answer[lowTempIdx] = index - lowTempIdx 
            stack.append([temp, index])

        return answer
temperatures = [73,74,75,71,69,72,76,73]
solulu = Solution()
print(solulu.dailyTemperatures2(temperatures))