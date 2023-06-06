s, k, h = map(int, input().split())

if s + k + h >= 100:
    print("OK")
else:
    min_s = min(s, k, h)

    if min_s == s:
        print("Soongsil")
    elif min_s == k:
        print("Korea")
    else:
        print("Hanyang")
