test_cases = int(input())
results = [sum(map(int, input().split())) for _ in range(test_cases)]
print(*results, sep="\n")
