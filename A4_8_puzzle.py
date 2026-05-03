import heapq

# The goal state: 0 is the empty space
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def solve_8_puzzle(start):
    # pq stores (f_score, moves_count, current_board)
    # f = moves_count + misplaced_tiles
    pq = [(0, 0, start)]
    visited = {start}

    while pq:
        f, moves, board = heapq.heappop(pq)

        if board == GOAL:
            return f"Solved in {moves} moves!"

        # 1. Find the empty space (0)
        empty_idx = board.index(0)
        r, c = divmod(empty_idx, 3)

        # 2. Try moving neighbors (Up, Down, Left, Right) into the empty space
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < 3 and 0 <= nc < 3:
                # Swap logic
                new_idx = nr * 3 + nc
                new_board = list(board)
                new_board[empty_idx], new_board[new_idx] = new_board[new_idx], new_board[empty_idx]
                new_board_tuple = tuple(new_board)

                if new_board_tuple not in visited:
                    visited.add(new_board_tuple)
                    
                    # h = count how many tiles are not in their goal position
                    h = sum(1 for i in range(9) if new_board_tuple[i] != 0 and new_board_tuple[i] != GOAL[i])
                    
                    # f = g + h
                    heapq.heappush(pq, (moves + 1 + h, moves + 1, new_board_tuple))

# Example usage:
start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
print(solve_8_puzzle(start_state))