import heapq


def prim_mst(graph, start):
    visited = {start}
    edges = [(w, start, v) for v, w in graph[start].items()]
    heapq.heapify(edges)
    mst, cost = [], 0

    while edges and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        cost += w
        for n, nw in graph[v].items():
            if n not in visited:
                heapq.heappush(edges, (nw, v, n))

    return mst, cost


def kruskal_mst(graph):
    parent = {n: n for n in graph}
    rank = {n: 0 for n in graph}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1
        return True

    seen, edges = set(), []
    for u in graph:
        for v, w in graph[u].items():
            key = tuple(sorted((u, v)))
            if key not in seen:
                seen.add(key)
                edges.append((w, u, v))

    mst, cost = [], 0
    for w, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == len(graph) - 1:
                break

    return mst, cost


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1}
    }

    print("Prim:", prim_mst(graph, 'A'))
    print("Kruskal:", kruskal_mst(graph))
