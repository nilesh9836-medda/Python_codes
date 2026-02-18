lst = list('abcde')
print('lst = ',lst)
print('traversal...')
for x in lst:
    print(x)
print('traversal with index...')
for i,x in enumerate(lst):
    print(i,' => ',x)
print('Reverse traversal...')
for x in reversed(lst):
    print(x)
print('Parallel iteration...')
a = [1,2,3,4,5]
for i,j in zip(a,lst):
    print(i,j)
