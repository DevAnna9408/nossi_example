# 재귀

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def fibo(n):
    if n == 1 or 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))

# 재귀함수는 점화식과 base case가 필요하다.
# 점화식은 자기 자신을 다시 호출하는 식이고, base case는 더 이상 자신을 호출할 수 없을 때 return 값이다.

# 재귀함수 전체 시간 복잡도 = 재귀 함수 호출 x 재귀 함수 하나 당의 시간 복잡도