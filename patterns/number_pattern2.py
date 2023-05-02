def pattern(rows):
    print("The pattern is:",end="\n\n")
    for i in range(rows,0,-1):
        for j in range(0,i):
            print(i,end=" ")
        print("\n")

rows=int(input("Enter the number of rows: "))
pattern(rows)
