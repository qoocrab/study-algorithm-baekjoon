numbers = input()

for i in numbers:
    if i != "0" and i != "1" and i != " ":
        print("F")
        break
else:
    print("S")
