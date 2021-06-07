# 게임 움직임 개발
row , col = map(int,input().split())
A , B , dir = map(int,input().split())

point = [[0]*col for x in range(row)]
point[A][B] = 1
#움직이는 방향 북 동 남 서
move_x = [-1,0,1,0]
move_y = [0,1,0,-1]

# 맵데이터 만들기
map_data = []
for i in range(row):
    map_data.append(list(map(int,input().split())))

#왼쪽으로 회전
def move_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0

while True:
    move_left()
    move_A = A + move_x[dir]
    move_B = B + move_y[dir]
    print("A",move_A,"B",move_B,"P",point)
    if point[move_A][move_B] == 0 and map_data[move_A][move_B] == 0:
        point[move_A][move_B] = 1
        A = move_A
        B = move_B
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        move_A = A - move_x[dir]
        move_B = B - move_y[dir]
        if map_data[move_A][move_B] == 0:
            A = move_A
            B = move_B
        else:
            break
        turn_time = 0
print(count)