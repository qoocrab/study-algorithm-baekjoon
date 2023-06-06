for i in range(int(input())):
    h, w = map(int, input().split())

    print((("X" * h) + "\n") * w)
