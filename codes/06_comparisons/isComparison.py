a = 'Python is fun!'
b = 'Python is fun!'
print(a == b) # returns True
print(a is b)    # returns False
a = [1, 2, 3, 4, 5]
b = a   # b references a
print(a == b)    # True
print(a is b)    # True
b = a[:]    # b now references a copy of a
print(a == b)    # True
print(a is b)    # False [!!]

a = 'short'
b = 'short'
c = 5
d = 5
print(a is b) # True
print(c is d) # True