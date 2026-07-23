class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        paths = []
        row_adder = col_adder = 0
        rows,cols = len(grid), len(grid[0])
        for i in range(len(grid)):
            path = []
            for j in range(len(grid[0])):
                if i==j==0:
                    col_adder += grid[i][j]
                if i == 0:
                    path.append(grid[i][j] + row_adder)
                    row_adder+=grid[i][j]
                elif j == 0:
                    path.append(grid[i][j] + col_adder)
                    col_adder += grid[i][j]
                else:
                    path.append(grid[i][j])
            paths.append(path)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                paths[i][j] = grid[i][j] + min(paths[i-1][j], paths[i][j - 1])
        return paths[rows - 1][cols - 1]
        
                