d, h, m = map(int, input().split())

time = ((d - 11) * 24 * 60 + h * 60 + m) - (11 * 60 + 11)

print(time if time >= 0 else -1)
