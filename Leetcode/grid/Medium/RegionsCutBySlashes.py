# 959. Regions Cut By Slashes

# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

# Given the grid grid represented as a string array, return the number of regions.

# Note that backslash characters are escaped, so a '\' is represented as '\\'.

# Example 1:
# Input: grid = [" /","/ "]
# Output: 2
# Example 2:
# Input: grid = [" /","  "]
# Output: 1
# Example 3:
# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        gridRows = len(grid)
        gridCols = len(grid[0])

        gridTwoRows = 3 * gridRows
        gridTwoCols = 3 * gridCols

        gridTwo = [ [0] * gridTwoCols for _ in range(gridTwoRows)]

        for r in range(gridRows):
            for c in range(gridCols):
                r2, c2 = r*3, c*3
                if grid[r][c] == "/":
                    gridTwo[r2][c2+2] = 1
                    gridTwo[r2+1][c2+1] = 1
                    gridTwo[r2+2][c2] = 1
                elif grid[r][c] == "\\":
                    gridTwo[r2][c2] = 1
                    gridTwo[r2+1][c2+1] = 1
                    gridTwo[r2+2][c2+2] = 1
        
        def dfs(r, c, visit):
            if (
                r < 0 or c < 0 
                or r == gridTwoRows 
                or c == gridTwoCols
                or gridTwo[r][c] != 0
                or (r,c) in visit
                ):
                return
            
            visit.add((r,c))
            neighbours = [ [r+1, c], [r, c+1], [r-1, c], [r, c-1] ]

            for neighbourRow, neighbourCol in neighbours:
                dfs(neighbourRow, neighbourCol, visit)
        
        visit = set()
        numberOfRegions = 0

        for r in range(gridTwoRows):
            for c in range(gridTwoCols):
                if gridTwo[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c, visit)
                    numberOfRegions += 1
        return numberOfRegions