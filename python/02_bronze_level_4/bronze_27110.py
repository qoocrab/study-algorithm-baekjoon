n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for num in numbers:
    if num < n:
        answer += num
    else:
        answer += n

print(answer)
