flag=0
num=int(input("Enter a number: "))
if num==0 and num==1:
    flag=1

for i in range(2,num//2):
    if num%i==0:
        flag=1

if flag==1:
    print("{} is not a prime number".format(num))
else:
    print("{} is a prime number".format(num))
