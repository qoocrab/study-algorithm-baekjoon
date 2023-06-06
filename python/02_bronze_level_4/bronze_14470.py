a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    print(c * abs(a) + d + b * e)
elif a == 0:
    print(d + b * e)
else:
    print((b - a) * e)
