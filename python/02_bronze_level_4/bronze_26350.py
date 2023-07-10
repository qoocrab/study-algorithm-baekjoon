for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    d = numbers[0]
    denominations = numbers[1:]

    is_good = all(denominations[i] >= 2 * denominations[i - 1] for i in range(1, d))
    print("Denominations:", *denominations)

    if is_good:
        print("Good coin denominations!\n")
    else:
        print("Bad coin denominations!\n")
