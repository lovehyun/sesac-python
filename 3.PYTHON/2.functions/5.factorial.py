def factorial(n):
    # for i in range(1, n+1):
    result = 1

    for i in range(n, 0, -1):
        result = result * i

    print(f'{n}펙토리알은 {result} 입니다.')

factorial(5)
factorial(7)
factorial(10)