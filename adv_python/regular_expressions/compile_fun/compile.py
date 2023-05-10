import re
count=0
pattern=re.compile("ab")
match=pattern.finditer("abaababa")
for m in match:
    count+=1
    print(m.start(),"...",m.end(),"...",m.group())
print("The number of occurrences: ",count)

'''
o/p:
0 ... 2 ... ab
3 ... 5 ... ab
5 ... 7 ... ab
The number of occurrences:  3
'''
