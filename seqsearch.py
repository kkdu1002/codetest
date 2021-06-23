def seq_search(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i+1
            
print("생성할 원소 개수 입력 후 찾고싶은 문자열 입력")
data = input().split()
n = int(data[0])
target = data[1]

print("원소 개수만큼 문자열 입력")
array = input().split()

print(seq_search(n,target,array))