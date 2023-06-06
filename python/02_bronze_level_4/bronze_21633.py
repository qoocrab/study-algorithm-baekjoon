k = int(input())

if 25 + k * 0.01 > 2000:
    print(2000.00)
elif 25 + k * 0.01 < 100:
    print(100.00)
else:
    print(f"{25 + k * 0.01:.2f}")
