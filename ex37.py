def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

num = int(input("N: "))
fibonacci(num)