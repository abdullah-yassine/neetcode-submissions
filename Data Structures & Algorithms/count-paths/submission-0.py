class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1 for _ in range(n)] for row in range(m)] # paths[i][j] = represent possible unique paths to get to i,j
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i][j - 1] + paths[i - 1][j]

        return paths[m - 1][n - 1]