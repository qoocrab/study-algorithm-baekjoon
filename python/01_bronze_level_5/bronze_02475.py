numbers = map(int, input().split())
verification = sum(num**2 for num in numbers) % 10
print(verification)
