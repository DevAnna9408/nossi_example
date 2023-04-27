# shortest_path_in_binary_matrix

from collections import deque

# https://leetcode.com/problems/shortest-path-in-binary-matrix/
def shortest_path_in_binary_matrix(grid):

    answer = -1
    row = len(grid)
    column = len(grid[0])

    if grid[0][0] != 0 or grid[row-1][column-1] != 0:
        return answer

    visited = [[False] * column for _ in range(row)]

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        cur_x, cur_y, cur_l = queue.popleft()

        # 목적지에 도착했을 때의 cur_l을 저장
        if cur_x == row - 1 and cur_y == column - 1:
            answer = cur_l
            break

        for i, j in direction:
            next_x = cur_x + i
            next_y = cur_y + j
            if 0 <= next_x < row and 0 <= next_y < column:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y, cur_l + 1))
                    visited[next_x][next_y] = True

    return answer

grid = [[0,0,0],[1,1,0], [1, 1, 0]]
print(shortest_path_in_binary_matrix(grid))