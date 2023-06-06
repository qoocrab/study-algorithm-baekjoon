case = 0

while True:
    numbers = list(map(int, input().split()))
    case += 1

    if len(numbers) == 1 and numbers[0] == 0:
        break
    elif len(numbers) % 2 != 0:
        print(
            f"Case {case}: {float((numbers[(len(numbers) + 1) // 2 - 1] + numbers[(len(numbers) + 1) // 2]) / 2):.1f}"
        )
    else:
        print(f"Case {case}: {float(numbers[len(numbers) // 2]):.1f}")
