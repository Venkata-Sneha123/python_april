import re
a="hello world good morning india 25"
b=re.match("hello",a)
print(b)

'''
o/p:
<re.Match object; span=(0, 5), match='hello'>
'''
