# grid는 1과 0으로 이루어진 지도를 표현하는 m x n의 이차원베열이다. 이 지도에 표시된 섬들의 총 갯수를 반환하시오
# 1은 육지, 0은 물이다. 섬이랑 수평과 수직으로 땅이 연결되어 있고, 주변은 물로 둘러쌓여 있는 것을 말한다.
# 또한 grid 4개의 가장가리는 모두 물로 둘러 쌓여있다고 가정하고 문제를 해결하라.

# number of island

from collections import deque

# https://leetcode.com/problems/number-of-islands/
def number_of_island(grid):

    # 섬의 갯수 카운트
    island = 0

    #행
    row = len(grid)

    #열
    column = len(grid[0])

    # 방문 할 예정인 이차원 배열을 모두 false로 초기화, 선언은 열 -> 행으로
    visited = [[False] * column for _ in range(row)]

    def bfs_island(x, y):

        # 상하좌우 순으로 방문할 때
        # 상 : x좌표 -1, y좌표는 그대로
        # 히: x좌표 + 1, y좌표는 그대로
        # 좌: x좌표는 그대로, y좌표 -1
        # 우: x좌표는 그대로, y좌표 +1
        move_x = [-1, 1, 0, 0]
        move_y = [0, 0, -1, 1]

        # bfs를 실행 할 때 마다 방문함을 True로 변경
        visited[x][y] = True

        # queue를 선언하고
        queue = deque()

        #queue에 x, y 좌표를 튜플 형태로 inqeue
        queue.append((x, y))

        # 대기열이 다 떨어질 때 까지
        while queue:
            
            # quque에서 한 개를 꺼내 튜플 형태로 저장하고
            cur_x, cur_y = queue.popleft()
            
            # 상하좌우 이동하면서 방문하기 위해 4번 반복 
            for i in range(4):
                next_x = cur_x + move_x[i]
                next_y = cur_y + move_y[i]

                # 방문하면 안되는 경우를 제외하고 반복
                
                # 열보다 작고 행보다 작으면서
                if 0 <= next_x < row and 0 <= next_y < column:
                    
                    # 좌표값이 0이면서 방문하지 않은 경우에만 아래 코드를 실행
                    if grid[next_x][next_y] != "0" and not visited[next_x][next_y]:
                        
                        # 방문함을 알리는 True를 선언하고
                        visited[next_x][next_y] = True
                        
                        # 대기얼에 다음 좌표를 넣음
                        queue.append((next_x, next_y))

    # 행열을 반복하면서
    for i in range(row):
        for j in range(column):
            
            # 만약 좌표 값이 1이고 방문하지 않았을 경우에만
            if grid[i][j] == 1 and not visited[i][j]:
                
                # bfs를 실행하고 섬의 갯수를 +1개
                bfs_island(i, j)
                island += 1

    return island
