alphabet = list()

for _ in range(97, 123):
    alphabet.append(0)

for c in input():
    alphabet[ord(c) - 97] += 1

print(*alphabet)
