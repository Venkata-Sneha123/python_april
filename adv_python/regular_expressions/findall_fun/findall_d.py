import re
a="hello world, good morning india 25"
b=re.findall("\d",a)
print(b)

'''
o/p:
['2', '5']
'''
