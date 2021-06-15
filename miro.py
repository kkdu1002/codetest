from collections import deque

n,m = map(int,input().split())

map_data = []
for i in range(n):
    map_data.append(list(map(int,input())))

move_x = [-1,1,0,0]
move_y = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map_data[nx][ny] == 0:
                continue
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = map_data[x][y] + 1
                queue.append((nx,ny))
    return map_data[n-1][m-1]
print(bfs(0,0))