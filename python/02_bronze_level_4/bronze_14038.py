game = list()

for i in range(6):
    game.append(input())

win = game.count("W")

if win >= 5:
    print("1")
elif win >= 3:
    print("2")
elif win >= 1:
    print("3")
else:
    print("-1")
