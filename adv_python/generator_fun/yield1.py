def fun():
    for i in range(1,10):
        yield i
y=fun()
for j in range(1,10):
    print(next(y))

'''
o/p:
1
2
3
4
5
6
7
8
9
'''
