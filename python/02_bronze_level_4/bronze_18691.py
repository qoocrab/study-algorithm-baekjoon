import math

T = int(input())
group = [1, 3, 5]

for _ in range(T):
    G, C, E = map(int, input().split())
    required_candies = max(0, E - C)
    distance = math.ceil(required_candies / group[G - 1])
    print(distance * group[G - 1])
