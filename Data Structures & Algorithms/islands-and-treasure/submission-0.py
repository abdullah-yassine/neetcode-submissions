class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 1. scan the grid for treasures and add to queue
        q = deque()
        row_size, col_size = len(grid), len(grid[0])
        INF = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        while q:
            row, col, dist = q.popleft()
            if col + 1 < col_size and grid[row][col + 1] == INF: #right
                grid[row][col + 1] = dist + 1
                q.append((row, col + 1, dist + 1))
            if row - 1 >= 0 and grid[row - 1][col] == INF: #up
                grid[row - 1][col] = dist + 1
                q.append((row - 1, col, dist + 1))
            if col - 1 >= 0 and grid[row][col - 1] == INF: #left
                grid[row][col - 1] = dist + 1
                q.append((row, col - 1, dist + 1))
            if row + 1 < row_size and grid[row + 1][col] == INF: # down
                grid[row + 1][col] = dist + 1
                q.append((row + 1, col, dist + 1))
            