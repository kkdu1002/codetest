n = int(input())
data = list(map(int,input().split()))
m = int(input())
search = list(map(int,input().split()))

for i in search:
    if i in data:
        print("yes",end=" ")
    else:
        print("no",end=" ")