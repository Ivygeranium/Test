def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = input("n을 입력하세요.")

print(fibonacci(n))
