# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left = 0
            right = len(row) - 1
            while left <= right:
                if row[right] < target:
                    break
                elif row[right] > target:
                    right -= 1
                elif row[left] < target:
                    left += 1
                else:
                    return True
        return False
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) - 1
        COLUMNS = len(matrix[0]) - 1
        top = 0
        bottom = ROWS

        while top <= bottom:
            row = (top+bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False
        row = (top+bottom) // 2
        left = 0
        right = COLUMNS

        while left <= right:
            column = (left+right) // 2
            if matrix[row][column] < target:
                left=column+1
            elif matrix[row][column] > target:
                right=column-1
            else: 
                return True

        return False 