from collections import defaultdict , deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['A','D','E']
graph['C'] = ['A','F']

print("BFS traversal:")
bfs(graph, 'A')
