t1, m1, t2, m2 = map(int, input().split())

time = t2 * 60 + m2 - (t1 * 60 + m1)

if time < 0:
    time += 24 * 60

print(time, time // 30)
