#Normal Fn. with Arguements
def addR(a,b,c,d):
    add = a+b+c
    return add
print(addR(10,20,30,40))

#Purpose of args
def addR(*argg):
    return sum(argg)
print(addR(10,20,30,40,52,75,8,5,26,15))
