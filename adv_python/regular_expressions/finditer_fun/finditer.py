import re
match=re.finditer("[abc]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[^abc]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[a-z]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[A-Z]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[0-9]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[a-zA-Z]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[a-zA-Z0-9]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("[^a-zA-Z0-9]","a7Sb@k9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())


'''
o/p:
0 ... 1 ... a
3 ... 4 ... b
1 ... 2 ... 7
2 ... 3 ... S
4 ... 5 ... @
5 ... 6 ... k
6 ... 7 ... 9
7 ... 8 ... #
8 ... 9 ... A
9 ... 10 ... z
0 ... 1 ... a
3 ... 4 ... b
5 ... 6 ... k
9 ... 10 ... z
2 ... 3 ... S
8 ... 9 ... A
1 ... 2 ... 7
6 ... 7 ... 9
0 ... 1 ... a
2 ... 3 ... S
3 ... 4 ... b
5 ... 6 ... k
8 ... 9 ... A
9 ... 10 ... z
0 ... 1 ... a
1 ... 2 ... 7
2 ... 3 ... S
3 ... 4 ... b
5 ... 6 ... k
6 ... 7 ... 9
8 ... 9 ... A
9 ... 10 ... z
4 ... 5 ... @
7 ... 8 ... #
'''
