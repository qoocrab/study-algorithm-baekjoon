apple = list()
banana = list()

for _ in range(3):
    apple.append(int(input()))

for _ in range(3):
    banana.append(int(input()))

a_score = apple[0] * 3 + apple[1] * 2 + apple[2]
b_score = banana[0] * 3 + banana[1] * 2 + banana[2]

if a_score > b_score:
    print("A")
elif a_score < b_score:
    print("B")
else:
    print("T")
