for _ in range(int(input())):
    p, t = map(int, input().split())
    p += (t // 4) - (t // 7)
    print(p)
