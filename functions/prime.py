def prime(num):
    flag=0
    for i in range(2,num//2):
        if num%i==0:
            flag=1
            break
    return flag

n=int(input("Enetr a number: "))
r=prime(n)
if r==1:
    print("{} is not a prime number".format(n))
else:
    print("{} is a prime number".format(n))

