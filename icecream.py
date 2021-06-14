def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if mapdata[x][y] == 0:
        mapdata[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m = map(int,input().split())
mapdata = []
count = 0

for i in range(n):
    mapdata.append(list(map(int,input())))

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)