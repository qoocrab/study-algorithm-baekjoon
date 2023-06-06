for _ in range(int(input())):
    n, a, b, c = map(int, input().split())

    if a + b + c >= 55 and a >= 35 * 0.3 and b >= 25 * 0.3 and c >= 40 * 0.3:
        print(n, a + b + c, "PASS")
    else:
        print(n, a + b + c, "FAIL")
