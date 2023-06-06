n, h, v = map(int, input().split())

print(max((n - v), v) * max((n - h), h) * 4)
