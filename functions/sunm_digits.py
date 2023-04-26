def sum_digits(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n//=10
    print("Sum of the digits = ",sum)        

n=int(input("Enter a number: "))
sum_digits(n)
