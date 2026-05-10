import heapq

def A_Star_Queens():
    pq = [(0, [])]

    while pq:
        f, board = heapq.heappop(pq)

        if len(board) == 4:
            return board
        
        for col in range(4):
            new_board = board + [col]

            h = 0

            for i in range(len(new_board)):
                for j in range(i+1, len(new_board)):
                    if new_board[i]==new_board[j] or abs(new_board[i] - new_board[j]) == j - i:
                        h+=1

            f_new = len(new_board) + h

            if h==0:
                heapq.heappush(pq, (f_new, new_board))

print("Solution : ", A_Star_Queens())