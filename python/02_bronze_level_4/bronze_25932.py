for _ in range(int(input())):
    num = list(map(int, input().split()))

    m = 18 in num
    z = 17 in num

    for i in num:
        print(i, end=" ")

    if m and z:
        print("both")
    elif m and not z:
        print("mack")
    elif not m and z:
        print("zack")
    else:
        print("none")

    print("")
