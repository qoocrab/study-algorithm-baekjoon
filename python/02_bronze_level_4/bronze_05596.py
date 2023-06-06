total_1 = list(map(int, input().split()))
total_2 = list(map(int, input().split()))

print(sum(total_2) if sum(total_1) < sum(total_2) else sum(total_1))
