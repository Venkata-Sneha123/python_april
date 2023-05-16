import re
a="hello world, $ Good Morning india 25 %"
b=re.findall("w.r",a)
print(b)
c=re.findall("o.d",a)
print(c)
d=re.findall("n.n",a)
print(d)
g=re.findall("n.i",a)
print(g)


'''
o/p:
['wor']
['ood']
['nin']
['ndi']
'''
