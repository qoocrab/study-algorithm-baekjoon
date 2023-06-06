x, l, r = map(int, input().split())

if x >= l and x >= r:
    print(r)
elif x <= l and x <= r:
    print(l)
else:
    print(x)
