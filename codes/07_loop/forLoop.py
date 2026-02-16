for i in [1,'a',2,'b',3,'c',4,'d',5,'e']:
    print(i,end="")
print()

for i in range(10):
    print(i,end=" ")
print()

for i in range(1,10):
    print(2**i,end=" ")
print()

a = [i for i in "Python"]
print(a)

a = [i**3 for i in range(1,11,+2)]
print(a)