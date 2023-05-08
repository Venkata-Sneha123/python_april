def f1():
    print("Hello")

f1()
f2=f1 
#del f1
f2()

print(id(f1))
print(id(f2))

'''
o/p:
Hello
Hello
140484907695552
140484907695552
'''
