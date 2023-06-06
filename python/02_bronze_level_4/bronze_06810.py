total = 0

for i, n in enumerate("9780921418"):
    if i % 2 == 1:
        total += int(n) * 3
    else:
        total += int(n)

for i in range(3):
    if i % 2 == 1:
        total += int(input()) * 3
    else:
        total += int(input())

print(f"The 1-3-sum is {total}")
