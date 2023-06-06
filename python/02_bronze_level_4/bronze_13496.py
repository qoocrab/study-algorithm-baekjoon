for i in range(int(input())):
    n, s, d = map(int, input().split())

    total = 0

    for j in range(n):
        di, vi = map(int, input().split())

        if di / s <= d:
            total += vi

    print(f"Data Set {i + 1}:\n{total}\n")
