# N * N크기의 공간에서 계획에 따라 A의 좌표움직이기
n = int(input())

x,y = 1,1

move = input().split()

move_row = [0,0,-1,1]
move_col = [-1,1,0,0]
movement = ['L','R','U','D']

for mo in move:
    for i in range(len(movement)):
        if mo == movement[i]:
            nx = x + move_row[i]
            ny = y + move_col[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
print(x,y)