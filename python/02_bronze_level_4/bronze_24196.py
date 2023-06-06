s = input()
i = 0
answer = ""

while i < len(s):
    answer += s[i]
    i += ord(s[i]) - ord("A") + 1

print(answer)
