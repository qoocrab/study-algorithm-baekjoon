n = int(input())

if n <= 5:
    print(n)
elif (n - 5) // 4 % 2 == 0:
    print(5 - ((n - 5) % 4))
else:
    print(1 + ((n - 5) % 4))
