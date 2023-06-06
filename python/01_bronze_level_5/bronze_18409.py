n = int(input())
s = input()

vowels = ["a", "e", "i", "o", "u"]
count = 0
for ch in s:
    if ch in vowels:
        count += 1

print(count)
