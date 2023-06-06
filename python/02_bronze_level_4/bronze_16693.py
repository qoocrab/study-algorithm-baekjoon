import math

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

if (r1 * r1 * math.pi) / p2 > a1 / p1:
    print("Whole pizza")
else:
    print("Slice of pizza")
