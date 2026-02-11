y = int(input("Enter a year to check if it Leap Year or Not: "))

if y % 100 == 0:
    if y % 400 == 0: print(f"{y} is Leap Year!!!")
    else: print("Not Leap Year")
else:
    if y % 4 == 0: print(f"{y} is Leap Year!!!")
    else: print("Not Leap Year")