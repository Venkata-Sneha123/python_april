def multi(a):
    def mul(b):
        def mu(c):
            return a*b*c
        return mu
    return mul

y=multi(10)(20)(2)
print(y)

'''
o/p:
400
'''
