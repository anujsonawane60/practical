# program to implient DFS traversal of a graph
# DFS traversal of a graph
from collections import defaultdict , deque
def dfs(graph, start):
    visited = set()
    stack = deque([start])
    visited.add(start)
    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

graph = defaultdict(list)
graph['A'] = ['B','C']
graph['B'] = ['A','D','E']
graph['C'] = ['A','F']

print("DFS traversal:")
dfs(graph, 'A')

