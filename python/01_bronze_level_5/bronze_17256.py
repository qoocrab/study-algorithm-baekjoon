cx, cy, cz = map(int, input().split())
ax, ay, az = map(int, input().split())

bx = cx - az
by = ay // cy
bz = cz - ax

print(bx, by, bz)
