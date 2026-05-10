import heapq

def prims_mst(n, adj):
    pq = [(0,0)]
    visited = [False]*n
    total_weight = 0

    while pq:
        w, u = heapq.heappop(pq)
        if not visited[u]:
            total_weight += w
            visited[u]=True
            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (weight, v))
    return total_weight

n = 4
adj = {
    0:[(1,1), (2,2)],
    1:[(0,1),(2,1)],
    2:[(0,2),(1,1),(3,4)],
    3:[(2,4)]
}

print(prims_mst(n,adj))
