import re
a="hello world, good morning india 25"
b=re.findall("india 25\Z",a)
print(b)

'''
o/p:
['india 25']
'''
