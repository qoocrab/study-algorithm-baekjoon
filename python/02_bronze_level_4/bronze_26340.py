for _ in range(int(input())):
    x, y, n = map(int, input().split())

    longer = max(x, y)
    shorter = min(x, y)

    for _ in range(n):
        longer, shorter = max(longer // 2, shorter), min(longer // 2, shorter)

    print(f"Data set: {x} {y} {n}")
    print(max(longer, shorter), min(longer, shorter))
    print()
