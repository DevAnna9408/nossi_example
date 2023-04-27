# 그래프 순회란, 그래프 탐색이라고도 부르고 그래파의 각 정점을 방문하는 과정이다.
# 깊이 우선 탐색과 너비 우선 탐색이 있다.

# 너비 우선 탐색 BFS

graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}

from collections import deque

def bfs_graph(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)

    return visited

bfs_graph(graph, 'A')

visited = []

def dfs_graph(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs_graph(graph)
    return visited

dfs_graph('A')
