def solve_n_queens(n, board=[]):
    # Base Case: All queens are placed
    if len(board) == n:
        return board

    # Try placing a queen in each column of the current row
    for col in range(n):
        # Constraint Check: Is this column or diagonal already attacked?
        if all(col != c and abs(col - c) != len(board) - i 
               for i, c in enumerate(board)):
            
            # Recursive Step: Branch into the next row
            result = solve_n_queens(n, board + [col])
            
            # If a solution was found deeper in the branch, return it
            if result: return result

    return None # Backtrack: No valid placement in this branch

n = 4
print(f"Solution for {n}-Queens:", solve_n_queens(n))