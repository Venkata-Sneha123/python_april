import re
a="hello world, good morning india 25"
b=re.findall("\Ahello",a)
print(b)

'''
o/p:
['hello']
'''
