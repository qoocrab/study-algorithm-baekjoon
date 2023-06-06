n, m = map(int, input().split())
original = [input() for _ in range(n)]
cnt = 0

input()

for i in range(n):
    negative = input()

    for j in range(m):
        if (original[i][j] == "B" and negative[j] == "W") or (
            original[i][j] == "W" and negative[j] == "B"
        ):
            continue
        else:
            cnt += 1

print(cnt)
