class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        row_size, col_size = len(grid), len(grid[0])
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 1:
                    perimeter += 4
                    if col - 1 >= 0 and grid[row][col - 1] == 1: # land to the left
                        perimeter -= 2
                    if row - 1 >= 0 and grid[row - 1][col] == 1: # land to the top
                        perimeter -= 2
        return perimeter
                    