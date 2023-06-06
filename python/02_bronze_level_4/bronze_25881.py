a, b = map(int, input().split())

for _ in range(int(input())):
    k = int(input())
    print(k, min(k, 1000) * a + max(k - 1000, 0) * b)
