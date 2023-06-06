min_list = list()

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a <= b:
        min_list.append(b)

if len(min_list) == 0:
    print(-1)
else:
    print(min(min_list))
