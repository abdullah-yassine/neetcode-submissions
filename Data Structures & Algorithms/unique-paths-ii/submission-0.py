class Solution:
# dp[i][j] = paths to (i,j). Obstacle -> 0, zero propagates.
#
#   grid          dp
#   0 0 0        1 1 1
#   0 0 0   ->   1 2 3
#   0 1 0        1 0 3     <- obstacle kills the middle
#
# 1D trick: row[j] is still "above", row[j-1] is already "left"
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(0, rows):
            for j in range(0, cols):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                elif i == 0 and j == 0:
                    paths[i][j] = 1
                else:
                    up = paths[i - 1][j] if i > 0 else 0
                    left = paths[i][j - 1] if j > 0 else 0
                    paths[i][j] = up + left
        return paths[rows - 1][cols - 1]