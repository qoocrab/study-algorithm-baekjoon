ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())
total = 0

if ca - cr < 0:
    total += ca - cr
if ba - br < 0:
    total += ba - br
if pa - pr < 0:
    total += pa - pr

print(abs(total))
