for _ in range(int(input())):
    c, p = map(int, input().split())
    print(c, p)
    print(p + max(c - 1, 0) * max(p - 2, 0))
