import re
a="hello world,hello good morning india 25"
b=re.search("morning",a)
print(b)

'''
o/p:
<re.Match object; span=(23, 30), match='morning'>
'''
