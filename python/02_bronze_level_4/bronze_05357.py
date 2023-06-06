for _ in range(int(input())):
    string = input()
    answer = ""

    for i, s in enumerate(string):
        if i == 0:
            answer += s
            continue
        elif s != string[i - 1]:
            answer += s

    print(answer)