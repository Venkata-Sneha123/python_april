import re
a="hello world,hello good morning india 25"
b=re.split("hello",a)
print(b)

'''
o/p:
['', ' world,', ' good morning india 25']
'''
