x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
if x>y>z:
    print(f"{x} is the largest")
elif y>x>z:
    print(f"{y} is the largest")
else:
    print(f"{z} is the largest")