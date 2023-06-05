score = int(input())

grades = {
    range(90, 101): "A",
    range(80, 90): "B",
    range(70, 80): "C",
    range(60, 70): "D",
    range(0, 60): "F",
}

for key, value in grades.items():
    if score in key:
        print(value)
        break
