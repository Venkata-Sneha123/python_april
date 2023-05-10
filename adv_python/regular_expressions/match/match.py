import re
p=input("Enter pattern to check:")
m=re.match(p,"hyderabad")
if m!= None:
    print("Match is available at the beginning of the String")
    print("Start Index:",m.start(), "and End Index:",m.end())
else:
    print("Match is not available at the beginning of the String")
    print(m)


'''
o/p:

Enter pattern to check:h
Match is available at the beginning of the String
Start Index: 0 and End Index: 1

Enter pattern to check:hyd
Match is available at the beginning of the String
Start Index: 0 and End Index: 3

Enter pattern to check:bad
Match is not available at the beginning of the String
None

Enter pattern to check:yder
Match is not available at the beginning of the String
None
'''
