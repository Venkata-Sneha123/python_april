unit=int(input("Enter a unit: "))
if unit<=100:
    amount=0
    print("amount=0")
elif unit>100 and unit<=200:
    amount=(unit-100)*5
    print("bill = {}".format(amount))
else:
    amount=500+(unit-200)*10 #500 means 5Rs.per unit for 101-200, so 100*5=500
    print("bill = {}".format(amount))

