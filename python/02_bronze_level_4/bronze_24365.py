a, b, c = map(int, input().split())

avg = (a + b + c) // 3

print((avg - b) + (avg - a) * 2)
