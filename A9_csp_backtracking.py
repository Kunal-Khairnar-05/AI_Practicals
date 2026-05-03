def is_safe_queens(board, row, col, n):
    """Check if placing queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """Backtracking: Place n queens on n x n board."""
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe_queens(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1


def nqueens(n):
    """Find all solutions for n-queens problem."""
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions


def is_safe_coloring(graph, coloring, node, color):
    """Check if assigning color to node is safe."""
    for neighbor in graph.get(node, []):
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True


def graph_coloring_backtrack(graph, coloring, nodes, colors, idx):
    """Backtracking: Assign colors to graph nodes."""
    if idx == len(nodes):
        return True

    node = nodes[idx]
    for color in colors:
        if is_safe_coloring(graph, coloring, node, color):
            coloring[node] = color
            if graph_coloring_backtrack(graph, coloring, nodes, colors, idx + 1):
                return True
            del coloring[node]

    return False


def graph_coloring(graph, num_colors):
    """Color graph using backtracking with given number of colors."""
    nodes = list(graph.keys())
    colors = list(range(num_colors))
    coloring = {}

    if graph_coloring_backtrack(graph, coloring, nodes, colors, 0):
        return coloring
    return None


if __name__ == "__main__":
    print("=== N-Queens Problem ===")
    n = 4
    solutions = nqueens(n)
    print(f"Solutions for {n}-queens: {len(solutions)} found")
    for sol in solutions:
        print(sol)

    print("\n=== Graph Coloring Problem ===")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    coloring = graph_coloring(graph, 2)
    print(f"Graph coloring with 2 colors: {coloring}")
