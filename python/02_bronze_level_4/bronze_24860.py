l1, l2 = map(int, input().split())
l3, l4 = map(int, input().split())
h1, h2, h3 = map(int, input().split())

print(l1 * l2 * h1 * h2 * h3 + l3 * l4 * h1 * h2 * h3)
