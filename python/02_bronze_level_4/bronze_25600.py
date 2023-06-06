max_score = 0

for i in range(int(input())):
    a, d, g = map(int, input().split())

    if a == d + g:
        score = 2 * a * (d + g)
    else:
        score = a * (d + g)

    if max_score < score:
        max_score = score

print(max_score)
