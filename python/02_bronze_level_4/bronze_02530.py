a, b, c = map(int, input().split())
d = int(input())

time = a * 3600 + b * 60 + c + d

print((time // 3600) % 24, (time % 3600) // 60, (time % 3600) % 60)
