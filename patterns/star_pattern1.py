def pattern(rows):
    print("The pattern is:")
    for i in range(1,rows+1):
        for j in range(rows,i-1,-1):
            print("*",end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
