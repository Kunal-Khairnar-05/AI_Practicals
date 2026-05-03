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




def prim_mst(graph, start_node):
    mst_edges = []
    visited = {start_node}
    # Priority Queue stores (weight, start_node, end_node)
    edges = [(weight, start_node, neighbor) 
             for neighbor, weight in graph[start_node].items()]
    heapq.heapify(edges)

    total_cost = 0

    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_cost += weight
            
            # Greedy Step: Add all edges from the new vertex to the queue
            for next_neighbor, next_weight in graph[v].items():
                if next_neighbor not in visited:
                    heapq.heappush(edges, (next_weight, v, next_neighbor))
                    
    return mst_edges, total_cost

# Example Graph: {Node: {Neighbor: Weight}}
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

mst, cost = prim_mst(graph, 'A')
print(f"MST Edges: {mst}")
print(f"Total MST Weight: {cost}")