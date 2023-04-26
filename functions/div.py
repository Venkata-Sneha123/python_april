def div(a,b):
    i=0 
    c=a
    while c>=b:
        c-=b
        i+=1
    print("Division of {},{} = {}".format(a,b,i))
    print("Modulus of {},{} = {}".format(a,b,c))


a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
div(a,b)
