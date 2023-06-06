x, y, z = map(int, input().split())
x_, y_, z_ = map(int, input().split())

if x == x_ and y == y_ and z == z_:
    print("A")
elif x_ >= x / 2 and y == y_ and z == z_:
    print("B")
elif y == y_ and z == z_:
    print("C")
elif y_ >= y / 2 and z == z_:
    print("D")
elif z == z_:
    print("E")
