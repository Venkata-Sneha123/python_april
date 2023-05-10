import re
match=re.finditer("a","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("a+","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("a*","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("a?","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("a{2}","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("a{2,3}","abaabaaab")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())


'''
o/p:
0 ... 1 ... a
2 ... 3 ... a
3 ... 4 ... a
5 ... 6 ... a
6 ... 7 ... a
7 ... 8 ... a
0 ... 1 ... a
2 ... 4 ... aa
5 ... 8 ... aaa
0 ... 1 ... a
1 ... 1 ... 
2 ... 4 ... aa
4 ... 4 ... 
5 ... 8 ... aaa
8 ... 8 ... 
9 ... 9 ... 
0 ... 1 ... a
1 ... 1 ... 
2 ... 3 ... a
3 ... 4 ... a
4 ... 4 ... 
5 ... 6 ... a
6 ... 7 ... a
7 ... 8 ... a
8 ... 8 ... 
9 ... 9 ... 
2 ... 4 ... aa
5 ... 7 ... aa
2 ... 4 ... aa
5 ... 8 ... aaa
'''
