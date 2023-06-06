n = int(input())
nums = list(map(float, input().split()))
total = sum([n**3 for n in nums])

print(total ** (1 / 3))
