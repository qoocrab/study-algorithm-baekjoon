n, m, k = map(int, input().split())
total = 0

if n - k <= n - m:
    total += n - k
else:
    total += n - m

if k <= m:
    total += k
else:
    total += m

print(total)
