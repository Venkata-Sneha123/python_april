def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("Inside function a={} b={}".format(a,b))

a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
swap(a,b)
print("Outside function a={} b={}".format(a,b))
