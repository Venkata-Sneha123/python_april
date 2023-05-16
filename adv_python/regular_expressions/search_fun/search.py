import re
a="hello world,hello good morning india 25"
b=re.search("hello",a)
print(b)

'''
o/p:
<re.Match object; span=(0, 5), match='hello'>
'''
