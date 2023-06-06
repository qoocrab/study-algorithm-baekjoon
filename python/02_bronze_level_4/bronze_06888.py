import math

s = int(input())
e = int(input())

for i in range(s, e + 1)[:: math.lcm(4, 2, 3, 5)]:
    print(f"All positions change in year {i}")
