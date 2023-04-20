num=int(input("Enter a number: "))
last=num%10
if last%3==0:
    print("Last digit[{}] of {} is divisible by {}".format(last,num,3))
else:
    print("Last digit[{}] of {} is not divisible by {}".format(last,num,3))

