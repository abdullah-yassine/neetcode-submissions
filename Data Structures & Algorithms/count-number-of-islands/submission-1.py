class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j, row_size, col_size):
            q = deque()
            q.append((i, j))
            while q:
                i, j = q.popleft()
                grid[i][j] = '0' # mark as visited
                if j + 1 < col_size and grid[i][j + 1] == '1': # right
                    q.append((i, j + 1))
                if i + 1 < row_size and grid[i + 1][j] == '1': # bottom
                    q.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == '1': # left
                    q.append((i, j - 1))
                if i - 1 >= 0 and grid[i - 1][j] == '1': # top
                    q.append((i - 1, j))


        row_size, col_size = len(grid), len(grid[0])
        islands = 0
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == '1':
                    bfs(i, j, row_size, col_size)
                    islands += 1
        return islands