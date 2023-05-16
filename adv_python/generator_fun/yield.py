def fun():
    for i in range(1,10):
        yield i

for j in range(1,10):
    print(next(fun()))

'''
o/p:
1
1
1
1
1
1
1
1
1
'''
