missing_alphabet = ord("A") * 26 + sum(range(26)) - sum(ord(c) for c in input())
print(chr(missing_alphabet))
