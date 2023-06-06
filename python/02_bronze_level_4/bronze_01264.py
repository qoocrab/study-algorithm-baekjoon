while True:
    string = input().lower()
    count = 0

    if string == "#":
        break

    print(len(list(filter(lambda c: c in "aeiou", string))))
