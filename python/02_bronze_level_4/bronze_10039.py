total = 0

for _ in range(5):
    score = int(input())
    total += max(40, score)

print(total // 5)
