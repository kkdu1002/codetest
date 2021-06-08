def iterative_factorial(a):
    result = 1
    for i in range(1,a+1):
        result *= i
    return result
    
def recursive_factorial(a):
    if a <= 1:
        return 1
    return a * recursive_factorial(a-1)

a = int(input())

print("반복문 factorial : ",iterative_factorial(a))
print("재귀함수 factorial : ",recursive_factorial(a))