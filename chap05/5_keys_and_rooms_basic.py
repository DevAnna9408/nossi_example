# 0번방부터 n-1번방 까지 총 n개의 방이 있다. 0번방을 제외 한 모든 방은 잠겨있다.
# 우리의 목표는 모든 방에 방문하는 것이다.
# 하지만 잠긴 방은 key가 없으면 방문할 수 없다.
# 각 방에 방문할 떄 별개의 열쇠뭉치를 찾을 수 도 있다.
# 각각의 열쇠에는 num이 쓰여져 있고, 해당 번호에 해당하는 방을 잠금 해제할 수 있다.
# 열쇠뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해 가져갈 수 있다.

# 문제에서 rooms배열이 주어지고 rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록이다.
# 모든 방을 방문할 수 있다면 true, 그렇지 않으면 false를 반환해라.

from collections import deque


def keys_and_rooms_dfs(rooms):
    visited = []

    def dfs(cur_v):
        visited.append(cur_v)

        for next_v in rooms[cur_v]:
            if next_v not in visited:
                dfs(next_v)

    return len(visited) == len(rooms)

print(keys_and_rooms_dfs([[1, 3], [2, 4], [0], [4], [], [3, 4]]))

def keys_and_rooms_bfs(rooms):
    visited = []

    def bfs(cur_v):
        queue = deque()
        queue.append(cur_v)
        visited.append(cur_v)

        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    queue.append(next_v)
                    visited.append(next_v)

    bfs(0)

    return len(visited) == len(rooms)

print(keys_and_rooms_bfs([[1, 3], [2, 4], [0], [4], [], [3, 4]]))