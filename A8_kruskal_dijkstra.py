import heapq

def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2]) # Greedy sort
    parent = list(range(n))
    
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i]) # Path compression
        return parent[i]

    mst_weight = 0
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_weight += w
    return mst_weight


def dijkstra(graph, start):
    # Initialize distances with infinity, start node with 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue stores (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If we found a longer path already, skip
        if current_dist > distances[u]:
            continue
            
        for v, weight in graph[u].items():
            distance = current_dist + weight
            
            # Greedy Step: If this new path is shorter, update and explore
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
                
    return distances

edges = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 5)]
print("Kruskal's MST weight:", kruskal_mst(4, edges))

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'D': 3},
    'D': {}
}

print(f"Shortest distances from A: {dijkstra(graph, 'A')}")