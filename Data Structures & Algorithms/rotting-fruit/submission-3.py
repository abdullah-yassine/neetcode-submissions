class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row_size, col_size = len(grid), len(grid[0])
        fresh_cnt = 0
        # 1. search for rotten bananas
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_cnt += 1
        time = 0
        changed = False
        while q and fresh_cnt > 0:
            snapshot_size = len(q)
            for _ in range(snapshot_size):
                row, col = q.popleft()
                if col + 1 < col_size and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    q.append((row, col + 1))
                    fresh_cnt -= 1
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    q.append((row - 1, col))
                    fresh_cnt -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    q.append((row, col - 1))
                    fresh_cnt -= 1
                if row + 1 < row_size and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    q.append((row + 1, col))
                    fresh_cnt -= 1
            time += 1
        
        return time if fresh_cnt == 0 else -1
        
