# 어떤 수 n이 1이 될때까지 반복수행하여 횟수의 최솟값출력
# 조건 1. n에서 1을 뺀다   2. n을 k로 나눈다
n,k = map(int,input().split())

count = 0

while True:
    if n % k == 0:
        n = n // k
        count += 1
    elif n == 1:
        break
    else:
        n -= 1
        count += 1
print(count)