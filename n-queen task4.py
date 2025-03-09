def safe(board, row, col, n):
    
    for i in range(row):  #check the column
        if board[i][col] == 1:
            return False
        
        
    i, j = row, col    
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
        
    return True

def solve_nqueen(board, row, n):
    
    if row == n:    
        print_solution(board, n)
        return True 
    
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueen(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


def n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueen(board, 0, n):
        print("solution does not exist")
        

def print_solution(board,n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()
    
    
    
n = 6
n_queen(n)



