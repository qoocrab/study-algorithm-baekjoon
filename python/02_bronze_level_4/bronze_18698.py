for _ in range(int(input())):
    n = input()

    if "U" not in n:
        print(0)
    elif "D" not in n:
        print(len(n))
    else:
        for i, s in enumerate(n):
            if s == "D":
                print(i)
                break
