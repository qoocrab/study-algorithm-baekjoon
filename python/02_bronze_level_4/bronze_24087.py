import math

s = int(input())
a = int(input())
b = int(input())

if s > a:
    print(250 + math.ceil((s - a) / b) * 100)
else:
    print(250)
