import heapq

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

# Example Graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'D': 3},
    'D': {}
}

print(f"Shortest distances from A: {dijkstra(graph, 'A')}")




def job_scheduling(jobs):
    # Sort by finish time (the second element in the tuple)
    jobs.sort(key=lambda x: x[1])
    
    selected_jobs = []
    last_finish_time = 0
    
    for start, finish in jobs:
        if start >= last_finish_time:
            selected_jobs.append((start, finish))
            last_finish_time = finish
            
    return selected_jobs

# Example: (start_time, finish_time)
tasks = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
print("Scheduled Jobs:", job_scheduling(tasks))