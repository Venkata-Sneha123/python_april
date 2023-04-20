n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))

if n1>n2 and n1>n3:
    print("{} is greater than {},{}".format(n1,n2,n3))
elif n2>n1 and n2>n3:
    print("{} is greater than {},{}".format(n2,n1,n3))
elif n3>n1 and n3>n2:
    print("{} is greater than {},{}".format(n3,n1,n2))

