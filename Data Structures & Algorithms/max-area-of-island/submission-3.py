class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j, row_size, col_size):
            q = deque()
            q.append((i, j))
            land = 0
            while q:
                i, j = q.popleft()
                land += 1
                grid[i][j] = 0 # mark as visited
                if j + 1 < col_size and grid[i][j + 1] == 1: # right
                    grid[i][j + 1] = 0
                    q.append((i, j + 1))
                if i + 1 < row_size and grid[i + 1][j] == 1: # bottom
                    grid[i + 1][j] = 0
                    q.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1: # left
                    grid[i][j - 1] = 0
                    q.append((i, j - 1))
                if i - 1 >= 0 and grid[i - 1][j] == 1: # top
                    grid[i - 1][j] = 0
                    q.append((i - 1, j))
            return land


        row_size, col_size = len(grid), len(grid[0])
        islands = 0
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    islands = max(bfs(i, j, row_size, col_size), islands)
        return islands
        