a=2
b=2
print(id(a))
print(id(b))
print(id(a)==id(b))
a=2
b=3
print(id(a))
print(id(b))
a='mohan'
b='Mohan'
print(id(a))
print(id(b))
print(id(a)==id(b))


'''
o/p:
140103426015504
140103426015504
True
140103426015504
140103426015536
140103407363184
140103407363056
False
'''
