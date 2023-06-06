n, d = map(int, input().split())
solve = [int(input()) for _ in range(n)]

for s in solve:
    print(s * d // sum(solve))
