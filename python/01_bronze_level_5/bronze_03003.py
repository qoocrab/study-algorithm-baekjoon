pieces = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

diff = [chess[i] - pieces[i] for i in range(6)]
print(*diff)
