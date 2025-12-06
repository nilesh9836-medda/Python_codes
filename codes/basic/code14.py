a=(float)(input("Enter the first number: "))
b=(float)(input("Enter the second number: "))
mode=input("Enter '+' for Addition\nEnter '-' for Substraction\nEnter '*' for Multiplication\nEnter '/' for Division\n (Enter): ")

if mode=='+':
    print("Result = %.2f"%(a+b))
elif mode=='-':
    print("Result = %.2f"%(a-b))
elif mode=='*':
    print("Result = %.2f"%(a*b))
elif mode=='/':
    if b==0:
        print("INFINITY!!!")
    else:
        print("Result = %.2f"%(a/b))
else:
    print("ERROR!!!!")
