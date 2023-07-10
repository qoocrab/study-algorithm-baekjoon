for _ in range(int(input())):
    total = 0

    for _ in range(int(input())):
        item, num, price = input().split()
        total += int(num) * float(price)

    print(f"${total:.2f}")
