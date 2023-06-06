import math

a, b = map(int, input().split())
gcd = math.gcd(b - a, b)
print((b - a) // gcd, b // gcd)
