# 264. Ugly Number II

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        allUglyNumbers = [1]

        idx2 = 0
        idx3 = 0
        idx5 = 0

        for idx in range(1, n):
            currentUglyNum = min(
                allUglyNumbers[idx2] * 2, 
                allUglyNumbers[idx3] * 3, 
                allUglyNumbers[idx5] * 5, 
            )

            allUglyNumbers.append(currentUglyNum)

            if currentUglyNum == allUglyNumbers[idx2] * 2:
                idx2 += 1

            if currentUglyNum == allUglyNumbers[idx3] * 3:
                idx3 += 1

            if currentUglyNum == allUglyNumbers[idx5] * 5:
                idx5 += 1
        
        return allUglyNumbers[n-1]