class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board[i])):
                if board[i][j] in num_set:
                    return False
                if board[i][j] != '.':
                    num_set.add(board[i][j])
        # Check each column
        for i in range(len(board)):
            num_set = set()
            for j in range(len(board[i])):
                if board[j][i] in num_set:
                    return False
                if board[j][i] != '.':
                    num_set.add(board[j][i])
        # Check each box
        grid_num_set = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i // 3, j // 3) not in grid_num_set:
                    grid_num_set[(i // 3, j // 3)] = set()
                if board[i][j] in grid_num_set[((i // 3, j // 3))]:
                    return False
                if board[i][j] != '.':
                    grid_num_set[(i // 3, j // 3)].add(board[i][j])
        return True
                
