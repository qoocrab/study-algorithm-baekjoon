n = int(input())
p = int(input())
answer = 0

if n >= 20:
    answer = min(max(p * 0.75, 0), max(p - 2000, 0))
elif n >= 15:
    answer = min(max(p * 0.9, 0), max(p - 2000, 0))
elif n >= 10:
    answer = min(max(p * 0.9, 0), max(p - 500, 0))
elif n >= 5:
    answer = max(p - 500, 0)
else:
    answer = p

print(int(answer))
