for _ in range(int(input())):
    a, b, c = map(int, input().split())
    count = 0

    if a >= 10:
        count += 1
    if b >= 10:
        count += 1
    if c >= 10:
        count += 1

    print(a, b, c)

    if count == 0:
        print("zilch")
    elif count == 1:
        print("double")
    elif count == 2:
        print("double-double")
    else:
        print("triple-double")

    print("")
