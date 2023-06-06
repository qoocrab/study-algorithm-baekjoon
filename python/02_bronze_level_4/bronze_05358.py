while True:
    try:
        name = input()
        answer = ""

        for n in name:
            if n == "i":
                answer += "e"
            elif n == "e":
                answer += "i"
            elif n == "I":
                answer += "E"
            elif n == "E":
                answer += "I"
            else:
                answer += n

        print(answer)
    except EOFError:
        break