def N_queens_CSP(n, board=[]):
    if len(board)==n:
        return board
    
    for col in range(n):
        if all(col != c and abs(col - c) != len(board) - i 
               for i, c in enumerate(board)):
            result = N_queens_CSP(n, board+[col])

            if result: return result

    return None
    
print(N_queens_CSP(4))