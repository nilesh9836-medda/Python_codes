a=(float)(input("Enter a number :"))
b=(float)(input("Enter a number :"))
add=a+b
sub=a-b
mult=a*b
div=a/b
mod=a%b
print(add)
print("addition:{0}, subtraction:{1}, multiplication:{2}, division:{3}, and mod:{4}".format(add,sub,mult,div,mod)) #print using format
print("Sum: %d, Diff: %d, Mult: %d, Div:%15.6f, Mod:%d"%(add,sub,mult,div,mod)) #Print using PADDING & PRECISION

print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format('Sum','Diff','Mult','Div'))
print('{0:<4} | {1:^4} | {2:^4} | {3:>4}'.format(add,sub,mult,div))