n = int(input())
factorial = 1

if n <= 1:
    print(1)
else:
    for i in range(1, n + 1):
        factorial *= i

    print(factorial % 10)
