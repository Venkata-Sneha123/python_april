def pattern(rows):
    print("The pattern is:")
    for i in range(0,rows):
        for k in range(0,rows-i):
            print(" ",end=" ")
        for j in range(0,i+1):
            print("*",sep=" ",end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
