x, k = map(int, input().split())

if k + k * 2 + k * 4 <= x:
    print(int(7 * k * 1000))
elif k + k / 2 + k * 2 <= x:
    print(int(7 / 2 * k * 1000))
elif k / 2 + k / 4 + k <= x:
    print(int(7 / 4 * k * 1000))
else:
    print(0)
