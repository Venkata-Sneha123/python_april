import re
a="hello world, $ Good Morning india 25 %"
b=re.findall("w...d",a)
print(b)
c=re.findall("G..d",a)
print(c)
g=re.findall("n..a",a)
print(g)


'''
o/p:
['world']
['Good']
['ndia']
'''
