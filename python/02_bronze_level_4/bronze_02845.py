l, p = map(int, input().split())
papers = list(map(int, input().split()))

for n in papers:
    print(n - (l * p), end=" ")
