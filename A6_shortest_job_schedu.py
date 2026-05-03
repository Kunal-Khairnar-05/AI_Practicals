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




def job_scheduling(jobs, t):
    # jobs is a list of (JobID, Deadline, Profit)
    # Sort jobs by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    result = [None] * t  # To store job IDs
    total_profit = 0

    for i in range(len(jobs)):
        # Try to find a free slot for this job (from deadline backwards)
        for j in range(min(t - 1, jobs[i][1] - 1), -1, -1):
            if result[j] is None:
                result[j] = jobs[i][0]
                total_profit += jobs[i][2]
                break
                
    return result, total_profit

# Example: (JobID, Deadline, Profit)
job_list = [('J1', 2, 100), ('J2', 1, 19), ('J3', 2, 27), ('J4', 1, 25), ('J5', 3, 15)]
scheduled_jobs, profit = job_scheduling(job_list, 3)

print(f"Scheduled Jobs: {[j for j in scheduled_jobs if j]}")
print(f"Total Profit: {profit}")