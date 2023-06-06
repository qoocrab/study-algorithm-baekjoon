number = input()

if number[1] == "0":
    a = int(number[:2])
    b = int(number[2:])
else:
    a = int(number[:1])
    b = int(number[1:])

print(a + b)
