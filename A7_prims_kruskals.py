import heapq

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

# Example usage
n = 4
adj = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2)],
    3: [(1, 5)]
}

edges = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 5)]
print("Prim's MST weight:", prim_mst(n, adj))
print("Kruskal's MST weight:", kruskal_mst(n, edges))