class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        row_size, col_size = len(board), len(board[0])
        def initial_append(r, c):
            if board[r][c] == 'O':
                board[r][c] = 'S'
                q.append((r,c))
        for col in range(col_size):
            initial_append(0,col)
            initial_append(row_size - 1, col)
        for row in range(row_size):
            initial_append(row, 0)
            initial_append(row, col_size - 1)
        while q:
            r,c = q.popleft()
            if c + 1 < col_size and board[r][c + 1] == 'O':
                board[r][c + 1] = 'S'
                q.append((r,c+1))
            if c - 1 >= 0 and board[r][c-1] == 'O':
                board[r][c-1] = 'S'
                q.append((r, c-1))
            if r + 1 < row_size and board[r + 1][c] == 'O':
                board[r + 1][c] = 'S'
                q.append((r + 1, c))
            if r - 1 >= 0 and board[r - 1][c] == 'O':
                board[r - 1][c] = 'S'
                q.append((r - 1, c))
        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'

        
