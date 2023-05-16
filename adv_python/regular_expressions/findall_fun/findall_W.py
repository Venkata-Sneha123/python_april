import re
a="hello world, $ good morning india 25 %"
b=re.findall("\W",a)
print(b)


'''
o/p:
[' ', ',', ' ', '$', ' ', ' ', ' ', ' ', ' ', '%']
'''
