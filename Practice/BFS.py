from collections import deque;

graph = {
    'A': ['B','C'],
    'B': ['A','D', 'E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

def bfs(graph, queue, visited=None):
    if visited is None:
        visited=set()
    
    if not queue:
        return
    
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    
    bfs(graph, queue, visited)

initial_queue = deque()
initial_queue.append('A')
bfs(graph, initial_queue)