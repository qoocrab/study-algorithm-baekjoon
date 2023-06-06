science = list()
social = list()

for _ in range(4):
    science.append(int(input()))

for _ in range(2):
    social.append(int(input()))

print(sum(science) - min(science) + sum(social) - min(social))
