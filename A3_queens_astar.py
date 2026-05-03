import heapq

def a_star_simple():
    # Priority Queue stores: (f_score, board)
    # f_score = len(board) + conflicts
    pq = [(0, [])]
    
    while pq:
        f, board = heapq.heappop(pq)
        
        # Goal: 4 queens placed with no conflicts
        if len(board) == 4:
            return board
        
        # Try every column for the next queen
        for col in range(4):
            new_board = board + [col]
            
            # Calculate Conflicts (Heuristic h)
            h = 0
            for i in range(len(new_board)):
                for j in range(i + 1, len(new_board)):
                    if new_board[i] == new_board[j] or abs(new_board[i] - new_board[j]) == j - i:
                        h += 1
            
            # g = len(new_board)
            # f = g + h
            f_new = len(new_board) + h
            
            # Only explore paths that are currently conflict-free to keep it "A*"
            if h == 0:
                heapq.heappush(pq, (f_new, new_board))

print("Solution:", a_star_simple())