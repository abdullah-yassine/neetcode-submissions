class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dup = set()
        dup_row = [set() for _ in range(9)]
        dup_col = [set() for _ in range(9)]
        i=j=j_resetter = i_resetter =0
        while i < 9 and j < 9:
            if board[i][j] in dup or board[i][j] in dup_row[i] or board[i][j] in dup_col[j]:
                return False
            
            if board[i][j] != ".":
                dup.add(board[i][j])
                dup_row[i].add(board[i][j])
                dup_col[j].add(board[i][j])
            if j in {2,5,8} and i in {2,5,8}: # transitioning to the next 3x3
                dup = set()
                if i == j == 8:
                    break
                if j == 8:
                    i = (i + 1) % 9
                else:
                    i = i - 2
                j = j_resetter = (j + 1) % 9
            else:
                j += 1
                if j - j_resetter == 3:
                    j = j_resetter
                    i += 1
        return True