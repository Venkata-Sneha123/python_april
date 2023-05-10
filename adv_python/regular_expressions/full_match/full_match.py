import re
p=input("Enter pattern to check:")
m=re.fullmatch(p,"hyderabad")
if m!= None:
    print("Match is available at the beginning of the String")
    print("Start Index:",m.start(), "and End Index:",m.end())
else:
    print("Match is not available at the beginning of the String")
print(m)


'''
o/p:

Enter pattern to check:hyd
Match is not available at the beginning of the String
None

Enter pattern to check:h
Match is not available at the beginning of the String
None

Enter pattern to check:hyderabad
Match is available at the beginning of the String
Start Index: 0 and End Index: 9
<re.Match object; span=(0, 9), match='hyderabad'>

Enter pattern to check:hyderbad
Match is not available at the beginning of the String
None
'''
