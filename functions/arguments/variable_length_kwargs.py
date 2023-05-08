def f1(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,"=",v)

f1(a=10,b=20,c=30)
f1(eid=1234,ename="sai",eaddress="hyd",esal=45000)

'''
o/p:
{'a': 10, 'b': 20, 'c': 30}
a = 10
b = 20
c = 30
{'eid': 1234, 'ename': 'sai', 'eaddress': 'hyd', 'esal': 45000}
eid = 1234
ename = sai
eaddress = hyd
esal = 45000
'''
