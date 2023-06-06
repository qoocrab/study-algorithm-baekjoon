m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())

left = m / g + l / a
right = m / s + r / b

if left > right:
    print("latmask")
else:
    print("friskus")
