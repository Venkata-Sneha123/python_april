import re
a="hello world, good morning india 25"
b=re.findall("\S",a)
print(b)

'''
o/p:
['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', ',', 'g', 'o', 'o', 'd', 'm', 'o', 'r', 'n', 'i', 'n', 'g', 'i', 'n', 'd', 'i', 'a', '2', '5']
'''
