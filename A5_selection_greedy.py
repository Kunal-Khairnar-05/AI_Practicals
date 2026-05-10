import heapq

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Greedy Choice: Assume the current position is the minimum
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Execution
data = [64, 25, 12, 22, 11]
print(f"Sorted Array: {selection_sort(data)}")




def prim_mst(n, adj):
    pq = [(0, 0)] # (weight, vertex)
    visited = [False] * n
    total_weight = 0
    
    while pq:
        w, u = heapq.heappop(pq)
        if not visited[u]:
            visited[u] = True
            total_weight += w
            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (weight, v))
    return total_weight
# Example Graph: {Node: {Neighbor: Weight}}
n = 4
adj = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2)],
    3: [(1, 5)]
}

print(f"Total MST Weight: {prim_mst(n, adj)}")