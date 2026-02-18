import copy

a = [1, 2, 3]
print(a)
b = a        # reference
print(b)
c = a.copy()    # shallow copy
print('c= ',c)
d = a[:]        # shallow copy
print('d = ',d)

x = [[1,2,3],[4,5,6],[7,8,9]]
deep = copy.deepcopy(x)
print(x)
