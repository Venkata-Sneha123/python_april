import re
a="hello world, good morning india 25"
b=re.sub("morning","afternoon",a)
print(b)

'''
o/P:
hello world, good afternoon india 25
'''
