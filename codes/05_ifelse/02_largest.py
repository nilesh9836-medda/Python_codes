a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b:
    if a > c: print(f"{a} is the greatest number among {a},{b},{c}")
    else: print(f"{c} is the greatest number among {a},{b},{c}")
else:
    if b > c: print(f"{b} is the greatest number among {a},{b},{c}")
    else: print(f"{c} is the greatest number among {a},{b},{c}")