def iseven(x):
    if x%2==0:
        return True
    else:
        return False

L=[2,3,4,5,6,7,8,9,10]
L1=list(filter(iseven,L))
print("Even Numbers are: ",L1)

'''
o/p:
Even Numbers are:  [2, 4, 6, 8, 10]
'''
