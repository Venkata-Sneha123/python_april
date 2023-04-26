def palindrome(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev

number=int(input("Enter a number: "))
result=palindrome(number)
if result==number:
    print(number,"is palindrome ")
else:
    print(number,"is not a palindrome")
