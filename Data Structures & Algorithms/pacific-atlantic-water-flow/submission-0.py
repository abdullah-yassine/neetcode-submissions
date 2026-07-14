class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(ocean):
            while q:
                row, col = q.pop()
                if col + 1 < col_size and heights[row][col] <= heights[row][col + 1] and (row, col + 1) not in ocean:
                    ocean.add((row, col + 1))
                    q.append((row, col + 1))
                if row + 1 < row_size and heights[row][col] <= heights[row + 1][col] and (row + 1, col) not in ocean:
                    ocean.add((row + 1, col))
                    q.append((row + 1, col))
                if col - 1 >= 0 and heights[row][col] <= heights[row][col - 1] and (row, col - 1) not in ocean:
                    ocean.add((row, col - 1))
                    q.append((row, col - 1))
                if row - 1 >= 0 and heights[row][col] <= heights[row - 1][col] and (row - 1, col) not in ocean:
                    ocean.add((row - 1, col))
                    q.append((row - 1, col))


        atlantic = set()
        pacific = set()
        row_size, col_size = len(heights), len(heights[0])
        q = deque()
        for col in range(col_size):
            q.append((0, col))
            pacific.add((0, col))
        for row in range(row_size):
            q.append((row, 0))
            pacific.add((row, 0))
        bfs(pacific)
        for row in range(row_size):
            q.append((row, col_size - 1))
            atlantic.add((row, col_size - 1))
        for col in range(col_size):
            q.append((row_size - 1, col))
            atlantic.add((row_size - 1, col))
        bfs(atlantic)
        return list(atlantic & pacific)
        

