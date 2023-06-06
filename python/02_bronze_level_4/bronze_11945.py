n, m = map(int, input().split())
matrix = list(input() for _ in range(n))

for row in matrix:
    print(row[::-1])
