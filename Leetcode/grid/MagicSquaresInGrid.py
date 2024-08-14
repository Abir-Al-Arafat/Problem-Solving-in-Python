# 840. Magic Squares In Grid

# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15. 

# Example 1:
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:

# while this one is not:
# In total, there is only one magic square inside the given grid.
# Example 2:

# Input: grid = [[8]]
# Output: 0

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        def isMagic(row, col):
            values = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
            
            # row sum
            for r in range(row, row+3):
                if sum(grid[r][col:col+3]) != 15:
                    return 0
            
            # col sum
            for c in range(col, col+3):
                if grid[row][c] + grid[row+1][c] + grid[row+2][c] != 15:
                    return 0
            
            # diagonal sum
            if (grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] != 15
                or
                grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] != 15):
                return 0

            return 1

        output = 0

        for row in range(ROWS-2):
            for col in range(COLUMNS-2):
                output += isMagic(row, col)
        
        return output