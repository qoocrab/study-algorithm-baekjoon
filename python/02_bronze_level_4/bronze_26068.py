count = 0

for _ in range(int(input())):
    d = input()
    if int(d[2:]) <= 90:
        count += 1

print(count)
