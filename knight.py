# 나이트 위치 옮길수있는 위치의 개수
data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1
move = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
count = 0
for movement in move:
    move_row = row + movement[0]
    move_col = col + movement[1]
    print("a",movement[0],"b",movement[1])
    if move_row >= 1 and move_col >= 1 and move_col <= 8 and move_row <= 8:
        count += 1
print(count)