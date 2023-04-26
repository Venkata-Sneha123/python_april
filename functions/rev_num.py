def reverse_number(num):
    rev=0
    while num > 0:
        rev=rev*10+num%10
        num//=10
    print("after reverse the number is:",rev)
    print("after reverse the number is: {}".format(rev))
    
n=int(input("Enter a number: "))
reverse_number(n)
