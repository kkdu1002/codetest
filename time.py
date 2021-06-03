# N시59분59초까지의 시간중에서 3이 하나라도 포함되는 모든 경우의 수
n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                count += 1
print(count)
