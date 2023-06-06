n, w, h, l = map(int, input().split())

if (w // l) * (h // l) <= n:
    print((w // l) * (h // l))
else:
    print(n)
