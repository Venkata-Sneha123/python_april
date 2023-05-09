s=lambda a,b,c:a if a>b and a>c else b if b>c else c

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))

print("Biggest of",a,b,c, " = ", s(a,b,c))

'''
o/p:
Enter a value: 5
Enter b value: 7
Enter c value: 2
Biggest of 5 7 2  =  7
'''
