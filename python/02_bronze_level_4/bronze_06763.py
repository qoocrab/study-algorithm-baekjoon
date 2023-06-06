l = int(input())
n = int(input())
diff = n - l
f = 0

if diff <= 0:
    print("Congratulations, you are within the speed limit!")
elif diff <= 20:
    f = 100
elif diff <= 30:
    f = 270
else:
    f = 500

if f != 0:
    print(f"You are speeding and your fine is ${f}.")
