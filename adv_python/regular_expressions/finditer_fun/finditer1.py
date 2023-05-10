import re
match=re.finditer("\s","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("\S","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("\d","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("\D","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("\w","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer("\W","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
match=re.finditer(".","a7Sb @k 9#Az")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())


'''
o/p:
4 ... 5 ...  
7 ... 8 ...  
0 ... 1 ... a
1 ... 2 ... 7
2 ... 3 ... S
3 ... 4 ... b
5 ... 6 ... @
6 ... 7 ... k
8 ... 9 ... 9
9 ... 10 ... #
10 ... 11 ... A
11 ... 12 ... z
1 ... 2 ... 7
8 ... 9 ... 9
0 ... 1 ... a
2 ... 3 ... S
3 ... 4 ... b
4 ... 5 ...  
5 ... 6 ... @
6 ... 7 ... k
7 ... 8 ...  
9 ... 10 ... #
10 ... 11 ... A
11 ... 12 ... z
0 ... 1 ... a
1 ... 2 ... 7
2 ... 3 ... S
3 ... 4 ... b
6 ... 7 ... k
8 ... 9 ... 9
10 ... 11 ... A
11 ... 12 ... z
4 ... 5 ...  
5 ... 6 ... @
7 ... 8 ...  
9 ... 10 ... #
0 ... 1 ... a
1 ... 2 ... 7
2 ... 3 ... S
3 ... 4 ... b
4 ... 5 ...  
5 ... 6 ... @
6 ... 7 ... k
7 ... 8 ...  
8 ... 9 ... 9
9 ... 10 ... #
10 ... 11 ... A
11 ... 12 ... z
'''
