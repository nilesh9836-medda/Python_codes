a=(1, 2, 3)
b=('a', 1, 'python', (1, 2))
#a[2]=3
print(type(a), b)

a=[1,2,3]
b=['a',1,'python',[1,2],(1,2)]
print(type(b), b)
a[2]=4
print(a)

a={1,0,3}
b={1,'a',(1,2)}
# c={1,[1,2,3],'a'}
print(type(b), b)
a.add(5)
print(a)

a= {1: 'one',
    2: 'two',
    3: 'three'}
b= {'a': [1,2,3],
    'b': 'a string'}
print(type(b), b)

print(len(b))
print(a==b)