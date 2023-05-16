def fun():
    yield 123
    yield "ts"
    yield 12.44

y=fun()
print(next(y))
print(next(y))
print(next(y))

'''
o/p:
123
ts
12.44
'''
