def mul(a,b):
    c=0
    d=b
    while d!=0:
        c+=a
        d-=1
    print("Multiplication of {},{} = {}".format(a,b,c))


a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
mul(a,b)
