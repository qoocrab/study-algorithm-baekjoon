row, column = map(int, input().split())

matrix_a = [list(map(int, input().split())) for _ in range(row)]
matrix_b = [list(map(int, input().split())) for _ in range(row)]

result = [[matrix_a[r][c] + matrix_b[r][c] for c in range(column)] for r in range(row)]

for r in result:
    print(*r)
