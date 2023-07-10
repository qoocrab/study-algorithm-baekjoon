for _ in range(int(input())):
    word, i, j = input().split()
    print(word[0 : int(i)] + word[int(j) :])
