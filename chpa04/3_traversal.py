# 트리순회, Traversal
# 트리탐색이라고도 하고, 트리의 각 노드를 방문하는 과정이다.
# 모든 노드를 한 번씩 방문해야 하므로 완전탐색이라고도 하고, 순회 방법으로는
# 너비 우선 탐색인 BFS, 깊이 우선 탐색인 DFS가 있다.

# 접근과 방문은 다르다. 접근은 단순 확인이지만 방문은 접근 후 무언가의 이벤트가 있는 것.

# BFS: 레벨에 따라 왼쪽에서 오른쪽으로 가까운 쪽 부터 수평으로 탐색하는 것을 BFS라고 한다. 너비 우선 탐색

from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return []

    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

# DFS: 왼쪽부터 간선을 따라 가장 깊은 곳 까지 방문 후 루트로 빠져나오고, 다시 다음 간선으로 이동하는 깊이 우선 탐색

def dfs(cur_node):
    if cur_node is None:
        return
    dfs(cur_node.left)
    dfs(cur_node.right)
