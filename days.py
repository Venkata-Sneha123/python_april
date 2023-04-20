day=int(input("Enter a number(1-7): "))
if day>=1 and day<=7:
    if day==1:
        print("{} is sunday".format(day)) 
    elif day==2:
        print("{} is monday".format(day))
    elif day==3:    
        print("{} is tuesday".format(day))
    elif day==4:
        print("{} is wednesday".format(day))
    elif day==5:
        print("{} is thursday".format(day))
    elif day==6:
        print("{} is friday".format(day))
    elif day==7:
        print("{} is saturday".format(day))
else:
    print("Invalid number")

